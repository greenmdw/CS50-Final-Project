"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.updateStatusBarText = exports.activate = void 0;
const vscode = require("vscode");
const numpyPreview_1 = require("./numpyPreview");
const numpyProvider_1 = require("./numpyProvider");
const utils_1 = require("./utils");
let myStatusBarItem;
function activate(context) {
    myStatusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
    myStatusBarItem.text = "Loading...";
    myStatusBarItem.show();
    context.subscriptions.push(myStatusBarItem);
    const extensionRoot = vscode.Uri.file(context.extensionPath);
    // Then register our provider
    const provider = new numpyProvider_1.NumpyCustomProvider(extensionRoot);
    context.subscriptions.push(vscode.window.registerCustomEditorProvider(numpyProvider_1.NumpyCustomProvider.viewType, provider, {
        webviewOptions: {
            enableFindWidget: true,
        }
    }));
    async function openTableView(uri) {
        const panel = vscode.window.createWebviewPanel('openWebview', // Identifies the type of the webview. Used internally
        'Table View', // Title of the panel displayed to the user
        vscode.ViewColumn.One, // Editor column to show the new webview panel in.
        {
            enableScripts: true //Set this to true if you want to enable Javascript. 
        });
        const _getResourcePath = utils_1.getResourcePath.bind(undefined, panel.webview, context);
        let tableCss = _getResourcePath('web/styles/table.css');
        var HTML = '';
        if (uri instanceof vscode.Uri) {
            HTML = await numpyPreview_1.NumpyPreview.getWebviewContents(uri.path, true, tableCss);
        }
        // console.log(HTML);
        panel.webview.html = HTML;
    }
    const tableViewCommmand = vscode.commands.registerCommand('numpy-viewer.openTableView', openTableView);
    context.subscriptions.push(tableViewCommmand);
    async function showArrayShape(uri) {
        var shapeInfo = 'unavailable';
        if (uri instanceof vscode.Uri) {
            shapeInfo = await numpyPreview_1.NumpyPreview.getWebviewContents(uri.path, true, '', true);
        }
        myStatusBarItem.text = shapeInfo;
        vscode.window.showInformationMessage(`Shape info: ${shapeInfo}`);
    }
    const arrayShapeCommmand = vscode.commands.registerCommand('numpy-viewer.showArrayShape', showArrayShape);
    context.subscriptions.push(arrayShapeCommmand);
}
exports.activate = activate;
function updateStatusBarText(text) {
    if (myStatusBarItem) {
        myStatusBarItem.text = text;
    }
}
exports.updateStatusBarText = updateStatusBarText;
// this method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map