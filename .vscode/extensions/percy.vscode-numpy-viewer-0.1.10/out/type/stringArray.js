"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.StringArray = void 0;
class StringArray {
    constructor(buffer, offset, eleSize) {
        this.offset = 0;
        this.eleSize = -1;
        this.data = [];
        this.buffer = buffer;
        this.offset = offset;
        this.eleSize = eleSize;
        const charArr = new Uint16Array(buffer, this.offset);
        // bytes num
        // const BYTES_PER_ELEMENT = eleSize * 4;
        const DOUBLE_BYTES_PER_ELEMENT = eleSize * 2;
        const stringNum = charArr.length / DOUBLE_BYTES_PER_ELEMENT;
        var begin = 0;
        var end = 0;
        end += DOUBLE_BYTES_PER_ELEMENT;
        for (var i = 0; i < stringNum; i++) {
            this.data.push("'" + String.fromCharCode.apply(null, Array.from(charArr.slice(begin, end))) + "'");
            begin += DOUBLE_BYTES_PER_ELEMENT;
            end += DOUBLE_BYTES_PER_ELEMENT;
        }
    }
    at(index) {
        if (index < 0 || index >= this.data.length) {
            new Error('Out of range');
        }
        return this.data[index];
    }
}
exports.StringArray = StringArray;
//# sourceMappingURL=stringArray.js.map