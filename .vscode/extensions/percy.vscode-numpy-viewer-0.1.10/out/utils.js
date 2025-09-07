"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.setPrecision = exports.getOption = exports.isLargerThanOne = exports.toMultiDimArray = exports.show2DArr = exports.makeTableHTML = exports.contentFormatting = exports.multiArrayToString = exports.wrapWithSqBr = exports.toCLikeArray = exports.toFortranAbsoluteIndex = exports.getResourcePath = exports.OSUtils = void 0;
const vscode = require("vscode");
const path = require("path");
const os = require('os');
const LOCAL_OS_TYPE = os.type();
class OSUtils {
    static isMacOS() {
        return LOCAL_OS_TYPE === OSUtils.type.macOS;
    }
    static isLinux() {
        return LOCAL_OS_TYPE === OSUtils.type.linux;
    }
    static isWindows() {
        return LOCAL_OS_TYPE === OSUtils.type.windows;
    }
}
exports.OSUtils = OSUtils;
OSUtils.type = {
    macOS: 'Darwin',
    linux: 'Linux',
    windows: 'Windows_NT',
};
function getResourcePath(webview, context, filePath) {
    //fix for windows because there path.join will use \ as separator and when we inline this string in html/js
    //we get specials strings e.g. c:\n
    // return `vscode-resource:${path.join(context.extensionPath, filePath).replace(/\\/g, '/')}`
    return `${webview.asWebviewUri(vscode.Uri.file(path.join(context.extensionPath, filePath).replace(/\\/g, '/')))}`;
}
exports.getResourcePath = getResourcePath;
function toFortranAbsoluteIndex(absoluteIdx, shape) {
    // e.g. to C like index  45 for shape (4, 5, 6)
    // [1][2][3] for shape (4, 5, 6) => 1 * (1) + 2 * (1 * 4) + 3 * (1 * 5 * 4)
    var res = 0;
    var base = 1;
    for (var i = 0; i < shape.length; i++) {
        base *= shape[i];
    }
    for (var i = 0; i < shape.length; i++) {
        // cLikeIdx.push(absoluteIdx % shape[-i]);
        base /= shape[shape.length - 1 - i];
        res += (absoluteIdx % shape[shape.length - 1 - i]) * base;
        absoluteIdx = Math.floor(absoluteIdx / shape[shape.length - 1 - i]);
    }
    return res;
}
exports.toFortranAbsoluteIndex = toFortranAbsoluteIndex;
function toCLikeArray(array, shape) {
    // walk arr
    var newArray = [];
    for (var i = 0; i < array.length; i++) {
        newArray.push(array[toFortranAbsoluteIndex(i, shape)]);
    }
    return newArray;
}
exports.toCLikeArray = toCLikeArray;
function wrapWithSqBr(s) {
    return '[' + s + ']';
}
exports.wrapWithSqBr = wrapWithSqBr;
function multiArrayToString(array, shape) {
    if (shape.length > 1) {
        const pieceNum = shape[0];
        // const pieceSize: number = array.length / pieceNum;
        var res = new Array(pieceNum);
        for (var i = 0; i < pieceNum; i++) {
            res[i] = multiArrayToString(array[i], shape.slice(1, shape.length));
        }
        return wrapWithSqBr(res.toString());
    }
    else {
        return wrapWithSqBr(array.toString());
    }
}
exports.multiArrayToString = multiArrayToString;
function contentFormatting(content, sl) {
    var res = content;
    for (var i = 0; i < sl - 1; i++) {
        // Break line
        var reg = new RegExp("\\]{" + (sl - 1 - i) + "},", "g");
        res = res.replace(reg, "$&<br/>");
        // Add indent (?<!\[)\[{1}(?!\[)
        var reg = new RegExp("(?<!\\[)\\[{" + (sl - 1 - i) + "}(?!\\[)", "g");
        res = res.replace(reg, "&nbsp".repeat(i + 1) + "$&");
    }
    return res;
}
exports.contentFormatting = contentFormatting;
function makeTableHTML(myArray, style = 'fixed_headers') {
    // Get table size
    const colNum = myArray[0].length;
    const rowNum = myArray.length;
    // Add table head, the first column for row ID
    var colContent = '';
    for (var i = 0; i < colNum; i++) {
        colContent += `<th>col ${i.toString()}</th>`;
    }
    var tableHead = `<thead>
      <tr>
      <td></td>
      ${colContent}
      </tr>
      </thead>
      `;
    // Add table body
    var rowContent = '';
    for (var i = 0; i < rowNum; i++) {
        var currentRow = `<td>row ${i.toString()}</td>`; // Add row ID
        for (var j = 0; j < myArray[i].length; j++) {
            currentRow += `<td>${myArray[i][j].toString()}</td>`;
        }
        rowContent += `<tr>${currentRow}</tr>`;
    }
    var tableBody = `<tbody>
    ${rowContent}
    </tbody>
    `;
    return `<table class=${style}>
    ${tableHead}
    ${tableBody}
    </table>`;
}
exports.makeTableHTML = makeTableHTML;
function show2DArr(array) {
    // Show array in an table
    // TODO: prettify it
    const tableHTML = makeTableHTML(array);
    return tableHTML;
}
exports.show2DArr = show2DArr;
function toMultiDimArray(array, shape) {
    if (shape.length > 1) {
        const pieceNum = shape[0];
        const pieceSize = array.length / pieceNum;
        var res = new Array(pieceNum);
        for (var i = 0; i < pieceNum; i++) {
            const begin = i * pieceSize;
            const end = array.length - (pieceNum - i - 1) * pieceSize;
            if (pieceSize !== 1) {
                res[i] = toMultiDimArray(array.slice(begin, end), shape.slice(1, shape.length));
            }
            else {
                res[i] = new Array([toMultiDimArray(array.slice(begin, end), shape.slice(1, shape.length))]);
            }
        }
        return res;
    }
    else {
        return array;
    }
}
exports.toMultiDimArray = toMultiDimArray;
function isLargerThanOne(element, index, array) {
    return element > 1;
}
exports.isLargerThanOne = isLargerThanOne;
function getOption(option) {
    let config = vscode.workspace.getConfiguration();
    return config.get(option);
}
exports.getOption = getOption;
function setPrecision(data) {
    data = data;
    let precision = getOption('vscode-numpy-viewer.printPrecision');
    if (precision > 0)
        for (var i = 0; i < data.length; i++)
            data[i] = parseFloat(data[i].toFixed(precision));
    return data;
}
exports.setPrecision = setPrecision;
//# sourceMappingURL=utils.js.map