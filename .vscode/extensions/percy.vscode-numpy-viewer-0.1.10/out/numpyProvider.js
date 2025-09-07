"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.NumpyCustomProvider = void 0;
const numpyPreview_1 = require("./numpyPreview");
class NumpyCustomProvider {
    constructor(extensionRoot) {
        this.extensionRoot = extensionRoot;
        this._previews = new Set();
    }
    openCustomDocument(uri) {
        return { uri, dispose: () => { } };
    }
    async resolveCustomEditor(document, webviewEditor) {
        const preview = new numpyPreview_1.NumpyPreview(this.extensionRoot, document.uri, webviewEditor);
        this._previews.add(preview);
        this.setActivePreview(preview);
        webviewEditor.onDidDispose(() => {
            this._previews.delete(preview);
        });
        webviewEditor.onDidChangeViewState(() => {
            if (webviewEditor.active) {
                this.setActivePreview(preview);
            }
            else if (this._activePreview === preview && !webviewEditor.active) {
                this.setActivePreview(undefined);
            }
        });
    }
    get activePreview() {
        return this._activePreview;
    }
    setActivePreview(value) {
        this._activePreview = value;
    }
}
exports.NumpyCustomProvider = NumpyCustomProvider;
NumpyCustomProvider.viewType = 'numpy.preview';
//# sourceMappingURL=numpyProvider.js.map