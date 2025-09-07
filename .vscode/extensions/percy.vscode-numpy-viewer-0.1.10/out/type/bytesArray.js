"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.BytesArray = void 0;
class BytesArray {
    constructor(buffer, offset, eleSize) {
        this.offset = 0;
        this.eleSize = -1;
        this.data = [];
        this.buffer = buffer;
        this.offset = offset;
        this.eleSize = eleSize;
        const charArr = new Uint8Array(buffer, this.offset);
        const BYTES_PER_ELEMENT = eleSize;
        const stringNum = charArr.length / BYTES_PER_ELEMENT;
        var begin = 0;
        var end = 0;
        end += BYTES_PER_ELEMENT;
        for (var i = 0; i < stringNum; i++) {
            this.data.push("b'" + String.fromCharCode.apply(null, Array.from(charArr.slice(begin, end))) + "'");
            begin += BYTES_PER_ELEMENT;
            end += BYTES_PER_ELEMENT;
        }
    }
    at(index) {
        if (index < 0 || index >= this.data.length) {
            new Error('Out of range');
        }
        return this.data[index];
    }
}
exports.BytesArray = BytesArray;
//# sourceMappingURL=bytesArray.js.map