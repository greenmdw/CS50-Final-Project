"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.BoolArray = void 0;
class BoolArray {
    constructor(buffer, offset) {
        this.offset = 0;
        this.eleSize = 1;
        this.eleNum = 0;
        this.data = [];
        this.buffer = buffer;
        this.offset = offset;
        const boolArr = new Uint8Array(buffer, this.offset);
        this.eleNum = boolArr.length;
        boolArr.forEach(element => {
            if (element === 1) {
                this.data.push(true);
            }
            else {
                this.data.push(false);
            }
        });
    }
    at(index) {
        if (index < 0 || index >= this.data.length) {
            new Error('Out of range');
        }
        return this.data[index];
    }
}
exports.BoolArray = BoolArray;
//# sourceMappingURL=boolArray.js.map