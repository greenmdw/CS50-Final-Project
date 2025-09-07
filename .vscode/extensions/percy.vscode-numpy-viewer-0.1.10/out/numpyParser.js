"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getFileSize = exports.fromArrayBuffer = exports.loadBuffer = exports.loadArrayBuffer = void 0;
// Modified from https://github.com/ludwigschubert/js-numpy-parser/blob/master/src/main.js
const fs = require("fs");
const bytesArray_1 = require("./type/bytesArray");
const boolArray_1 = require("./type/boolArray");
const stringArray_1 = require("./type/stringArray");
const objectArray_1 = require("./type/objectArray");
const complexArray_1 = require("./type/complexArray");
var stringArrEleSize = -1;
var bytesArrEleSize = -1;
function loadArrayBuffer(file) {
    const buffer = fs.readFileSync(file);
    return new Uint8Array(buffer).buffer; // only needed for node conversion
}
exports.loadArrayBuffer = loadArrayBuffer;
function loadBuffer(file) {
    return fs.readFileSync(file);
}
exports.loadBuffer = loadBuffer;
class DataViewReader {
    constructor(dataView) {
        this.dataView = dataView;
        this.offset = 0;
        this.dataView = dataView;
    }
    /* Variable length accessors */
    readBytes(length) {
        const buffer = new DataView(this.dataView.buffer, this.offset, length);
        this.offset += length;
        return buffer;
    }
    readAndASCIIDecodeBytes(length) {
        const array = new Uint8Array(this.dataView.buffer, this.offset, length);
        this.offset += length;
        return this._decodeASCIIByteArray(array);
    }
    /* Fixed length accessors */
    readUint8() {
        const value = this.dataView.getUint8(this.offset);
        this.offset += Uint8Array.BYTES_PER_ELEMENT;
        return value;
    }
    readUint16(littleEndian = false) {
        const value = this.dataView.getUint16(this.offset, littleEndian);
        this.offset += Uint16Array.BYTES_PER_ELEMENT;
        return value;
    }
    readUint32(littleEndian = false) {
        const value = this.dataView.getUint32(this.offset, littleEndian);
        this.offset += Uint32Array.BYTES_PER_ELEMENT;
        return value;
    }
    readBigUInt64(littleEndian = false) {
        const value = this.dataView.getBigUint64(this.offset, littleEndian);
        this.offset += BigUint64Array.BYTES_PER_ELEMENT;
        return value;
    }
    /* Helpers */
    _decodeASCIIByteArray(array) {
        const characters = [];
        for (const byte of array) {
            const char = String.fromCharCode(byte);
            characters.push(char);
        }
        return characters.join('');
    }
}
function fromArrayBuffer(buffer) {
    const reader = new DataViewReader(new DataView(buffer));
    // comments are taken from https://docs.scipy.org/doc/numpy-1.14.1/neps/npy-format.html#format-specification-version-1-0
    // "The first 6 bytes are a magic string: exactly "x93NUMPY""
    const magicByte = reader.readUint8();
    const magicWord = reader.readAndASCIIDecodeBytes(5);
    if (magicByte !== 0x93 || magicWord !== 'NUMPY') {
        throw new Error(`unknown file type: "${magicByte}${magicWord}"`);
    }
    // "The next 1 byte is an unsigned byte: the major version number of the file format, e.g. x01.""
    const versionMajor = reader.readUint8();
    // "The next 1 byte is an unsigned byte: the minor version number of the file format, e.g. x00."
    const versionMinor = reader.readUint8();
    // Parse header length. This depends on the major file format version as follows:
    let headerLength;
    if (versionMajor <= 1) {
        // "The next 2 bytes form a little-endian unsigned short int: the length of the header data HEADER_LEN."
        headerLength = reader.readUint16(true);
    }
    else {
        // "The next 4 bytes form a little-endian unsigned int: the length of the header data HEADER_LEN."
        headerLength = reader.readUint32(true);
    }
    /* "The next HEADER_LEN bytes form the header data describing the array’s format.
    It is an ASCII string which contains a Python literal expression of a dictionary.
    It is terminated by a newline (‘n’) and padded with spaces (‘x20’) to make the total
    length of the magic string + 4 + HEADER_LEN be evenly divisible by 16." */
    const preludeLength = 6 + 4 + headerLength;
    if (preludeLength % 16 !== 0) {
        console.warn(`NPY file header is incorrectly padded. (${preludeLength} is not evenly divisible by 16.)`);
    }
    const headerStr = reader.readAndASCIIDecodeBytes(headerLength);
    const header = parseHeaderStr(headerStr);
    var order = 'C';
    if (header.fortran_order) {
        order = 'F';
        // throw new Error('NPY file is written in Fortran byte order, support for this byte order is not yet implemented.');
    }
    // Intepret the bytes according to the specified dtype
    var data;
    const { constructor: ctor, typeDesc: td } = typedArrayConstructorForDescription(header.descr);
    switch (td) {
        case 'complex':
            var complexArray = new complexArray_1.ComplexArray(buffer, reader.offset);
            data = complexArray.data;
            break;
        case 'string':
            var stringArray = new stringArray_1.StringArray(buffer, reader.offset, stringArrEleSize);
            data = stringArray.data;
            break;
        case 'bytes':
            var bytesArray = new bytesArray_1.BytesArray(buffer, reader.offset, bytesArrEleSize);
            data = bytesArray.data;
            break;
        case 'bool':
            var boolArray = new boolArray_1.BoolArray(buffer, reader.offset);
            data = boolArray.data;
            // if (boolArray.eleNum > MAX_OUTPUT_BOOL_LIMIT) {
            //   data = new Uint8Array(buffer, reader.offset);
            //   console.log('[+] true and false have been replaced with numbers');
            // }
            break;
        case 'python object':
            // Solve dict type data
            var objectArray = new objectArray_1.ObjectArray(buffer, reader.offset);
            data = objectArray.data;
            break;
        case 'float16':
            var fp16Array = new Float16Array(buffer, reader.offset);
            data = fp16Array.data;
            break;
        default:
            data = new ctor(buffer, reader.offset);
    }
    // console.log('[+] Data has been loaded successfully', data);
    // Return object with same signature as NDArray expects: {data, shape}
    return { data: data, shape: header.shape, order: order, decr: td };
}
exports.fromArrayBuffer = fromArrayBuffer;
function parseHeaderStr(headerStr) {
    const jsonHeader = headerStr
        .replace('L', '') // string array (116L,) -> (116,)
        .replace('U', 'str')
        .replace('S', 'bytes')
        .toLowerCase() // boolean literals: False -> false
        .replace('(', '[').replace('),', ']') // Python tuple to JS array: (10,) -> [10,]
        .replace('[,', '[1,]').replace(',]', ']') // implicit dimensions: [10,] -> [10]
        .replace(/'/g, '"'); // single quotes -> double quotes
    // console.log(jsonHeader);
    return JSON.parse(jsonHeader);
}
/* TODO: 1. add judgement for big end and little end
         2. support more types
*/
function typedArrayConstructorForDescription(dtypeDescription) {
    /* 'dtype' description strings consist of three characters, indicating one of three
       properties each: byte order, data type, and byte length.
       Byte order: '<' (little-endian), '>' (big-endian), or '|' (not applicable)
       Data type: 'u' (unsigned), 'i' (signed integer), 'f' (floating)
       Byte Length: 1, 2, 4 or 8 bytes
       Note that for 1 byte dtypes there is no byte order, thus the use of '|' (not applicable).
       Data types are specified in numpy source:
       https://github.com/numpy/numpy/blob/8aa121415760cc6839a546c3f84e238d1dfa1aa6/numpy/core/_dtype.py#L13
     */
    switch (dtypeDescription) {
        // Python object
        case '|o':
            return { constructor: String, typeDesc: 'python object' };
            ;
        // Unsigned Integers
        case '|u1':
            return { constructor: Uint8Array, typeDesc: 'unsigned int8' };
        case '<u2':
            return { constructor: Uint16Array, typeDesc: 'unsigned int16' };
        case '<u4':
            return { constructor: Uint32Array, typeDesc: 'unsigned int32' };
            ;
        case '<u8':
            return { constructor: BigUint64Array, typeDesc: 'unsigned int64' };
        // Integers
        case '|i1': // "byte"
            return { constructor: Int8Array, typeDesc: 'signed int8' };
        case '<i2': // "short"
            return { constructor: Int16Array, typeDesc: 'signed int16' };
        case '<i4': // "intc"
            return { constructor: Int32Array, typeDesc: 'signed int32' };
        case '<i8': // "longlong" (??)
            return { constructor: BigInt64Array, typeDesc: 'signed int64' };
        // Floating
        case '<f2': // "half"
            return { constructor: Float16Array, typeDesc: 'float16' };
        case '<f4': // "single"
            return { constructor: Float32Array, typeDesc: 'float32' };
        case '<f8': // "double" "longfloat"
            return { constructor: Float64Array, typeDesc: 'float64' };
        case '|b1':
            return { constructor: Boolean, typeDesc: 'bool' };
        case '<c16':
            return { constructor: Float64Array, typeDesc: 'complex' };
        // No support for ComplexFloating, on-number types (flexible/character/void...) yet
        default:
            // check whether is string array
            if (dtypeDescription.startsWith('<str')) {
                const size = parseInt(dtypeDescription.slice(4));
                console.log('[+] String Array, element size is', size);
                stringArrEleSize = size;
                return { constructor: String, typeDesc: 'string' };
            }
            if (dtypeDescription.startsWith('|bytes')) {
                const size = parseInt(dtypeDescription.slice(6));
                console.log('[+] Bytes Array, element size is', size);
                bytesArrEleSize = size;
                return { constructor: String, typeDesc: 'bytes' };
            }
            throw new Error('Unknown or not yet implemented numpy dtype description: ' + dtypeDescription);
    }
}
function getFileSize(path) {
    const stats = fs.statSync(path);
    const fileSizeInBytes = stats.size;
    const fileSizeInMegabytes = fileSizeInBytes / (1024 * 1024);
    return fileSizeInMegabytes;
}
exports.getFileSize = getFileSize;
/* FP16  experimental feature */
function convertFloat16ToNumber(buffer, offset, littleEndian = true) {
    const uint16 = buffer.getUint16(offset, littleEndian);
    const sign = (uint16 & 0x8000) >> 15;
    const exponent = (uint16 & 0x7C00) >> 10;
    const fraction = uint16 & 0x03FF;
    if (exponent === 0) {
        return (sign ? -1 : 1) * Math.pow(2, -14) * (fraction / 0x0400);
    }
    else if (exponent === 0x1F) {
        return fraction ? NaN : ((sign ? -1 : 1) * Infinity);
    }
    return (sign ? -1 : 1) * Math.pow(2, exponent - 15) * (1 + fraction / 0x0400);
}
class Float16Array {
    constructor(buffer, byteOffset = 0) {
        this.data = [];
        this.buffer = buffer;
        this.view = new DataView(buffer, byteOffset);
        this.length = (buffer.byteLength - byteOffset) / 2;
        this.data = new Array(this.length);
        for (let i = 0; i < this.length; i++) {
            this.data[i] = this.get(i);
            // console.log("fp16 construction", this.data[i]);
        }
    }
    get(index) {
        return convertFloat16ToNumber(this.view, index * 2);
    }
    at(index) {
        if (index < 0 || index >= this.data.length) {
            new Error('Out of range');
        }
        return this.data[index];
    }
}
//# sourceMappingURL=numpyParser.js.map