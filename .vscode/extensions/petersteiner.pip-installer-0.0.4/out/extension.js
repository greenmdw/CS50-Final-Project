"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = void 0;
const vscode = require("vscode");
function activate(context) {
    let disposable = vscode.commands.registerCommand('pip-installer.getMissingImports', async () => {
        let editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showInformationMessage('No file open');
            return;
        }
        let document = editor.document;
        let missingImports = getMissingImports(document);
        if (missingImports.length === 0) {
            vscode.window.showInformationMessage('No missing imports found');
            return;
        }
        let message = `Missing imports found: ${missingImports.join(', ')}. Do you want to install these packages?`;
        let installButton = { title: 'Install' };
        let result = await vscode.window.showInformationMessage(message, installButton);
        if (result === installButton) {
            let terminal = vscode.window.createTerminal();
            terminal.show();
            terminal.sendText(`pip3 install ${missingImports.join(' ')}`);
        }
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
function getMissingImports(document) {
    let missingImports = [];
    let diagnostics = vscode.languages.getDiagnostics(document.uri);
    let importDiagnostics = diagnostics.filter(d => d.source === 'Pylance' && d.message.startsWith('Import'));
    importDiagnostics.forEach(d => {
        let importName = d.message.split('"')[1];
        importName = importName.split(".")[0];
        missingImports.push(importName);
    });
    // remove duplicates
    missingImports = missingImports.filter((item, index) => missingImports.indexOf(item) === index);
    return missingImports;
}
//# sourceMappingURL=extension.js.map