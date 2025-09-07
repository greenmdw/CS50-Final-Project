"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ComplexArray = void 0;
// An complex number element a + bj contains two numner a and b.
class Complex {
    constructor(real, virtual) {
        this.real = real;
        this.virtual = virtual;
        this.toString = () => {
            return `${this.real}+${this.virtual}j`;
        };
    }
}
class ComplexArray {
    constructor(buffer, offset) {
        this.offset = 0;
        this.eleSize = -1;
        this.data = [];
        this.buffer = buffer;
        this.offset = offset;
        var temp_data = new Float64Array(buffer, offset);
        for (var i = 0; i < Math.ceil(temp_data.length / 2); i++) {
            const ele = new Complex(temp_data[2 * i], temp_data[2 * i + 1]);
            this.data.push(ele);
        }
    }
    at(index) {
        if (index < 0 || index >= this.data.length) {
            new Error('Out of range');
        }
        return this.data[index];
    }
}
exports.ComplexArray = ComplexArray;
//# sourceMappingURL=complexArray.js.map