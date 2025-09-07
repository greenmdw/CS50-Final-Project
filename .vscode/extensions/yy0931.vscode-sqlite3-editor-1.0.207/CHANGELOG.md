# Changelog
# 1.0.207
- Specified minimum and maximum values for all numeric configurations to prevent errors, including the error "too large to fit in MessagePack 64-bit integer format".

# 1.0.206
- Changed how the extension displays the currently visible user query (the user-input SELECT statement).
  It is now integrated into the table selector, and a button to save a query as a view has also been added.
- Added hover documentation for some SQL keywords.
- Made the Monaco editor fall back to basic text areas when loading fails. [#76](https://github.com/yy0931/sqlite3-editor/issues/76)
- Removed the "Open in Excel" feature to prevent false positives from antivirus software. [#78](https://github.com/yy0931/sqlite3-editor/issues/78)

# 1.0.205
- Fixed a bug where combining the "group by" and "column filter" features could throw a "datatype mismatch" error. [#75](https://github.com/yy0931/sqlite3-editor/issues/75)
- Fixed a bug where row counts were computed incorrectly when the "group by" feature was used, allowing scrolling beyond the actual end of the table.

# 1.0.204
- Updated the bundled SQLite to version 3.49.1.

# 1.0.203
- Fixed a bug where opening a WAL-mode database in a virtual workspace could cause `UNKNOWN errno: -4094` errors under certain conditions. [#68](https://github.com/yy0931/sqlite3-editor/issues/68)
- Added a mechanism to display a detailed error messages for file system errors by calling the OS filesystem API as a fallback. [#68](https://github.com/yy0931/sqlite3-editor/issues/68)
- Fixed a bug where opening a database as a gitGit-diff view could cause `Unexpected end of JSON input` errors.

# 1.0.202
- Added an `Open <table name>` button to the "Statement executed successfully" message, which is shown when executing a non-SELECT query in the query editor. The button appears only if the updated table is different from the currently visible table. [#69](https://github.com/yy0931/sqlite3-editor/issues/69)
- Fixed the `Execute Selection` command to display the table after executing a SELECT statement. [#69](https://github.com/yy0931/sqlite3-editor/issues/69)
- Updated the bundled SQLite to version 3.49.0.

# 1.0.201
- Added ARMv6 musl executable.
- Slightly improved the extension's startup time by optimizing communication between the extension host and the webview.

# 1.0.200
- Added the Table View Settings window for visually configuring some UI settings. You can access it from the Other Tools menu.
- Improved the styling of cells containing right-aligned numbers.
- Removed the configuration `sqlite3-editor.ui.wrapTableHeader`, which had the same effect as `"sqlite3-editor.ui.tableHeaderMaxLines": 1` and has been deprecated since version 1.0.140.

# 1.0.199
- Improved the JSON import feature to preserve data types rather than converting all values to TEXT.
- Improved the arrow key navigation in the table selector for databases that have shadow tables.

# 1.0.198
- Fixed errors triggered by the command palette items "SQLite3 Editor: Select Table" and "SQLite3 Editor: Go to Table/Row".

# 1.0.197
- Updated the bundled SQLite to version 3.47.2.
- Removed the opt-in telemetry because we have stopped adding new features to this extension. The telemetry feature in older versions of the extension will also no longer work, as the server instance will be removed.

# 1.0.196
- Changed the current working directory of the database connection process to match the database file's directory. [#66](https://github.com/yy0931/sqlite3-editor/issues/66)
- Improved the behavior of middle mouse button scrolling on the table, introduced in v1.0.195.
- Fixed a bug where the settings links in the history pane failed to open the settings page.
- Fixed a bug where, after executing an ALTER TABLE statement from another process, the extension sometimes failed to display the updated column names.

# 1.0.195
- Added support for scrolling with middle mouse button.

# 1.0.194
- Improved error handling.

# 1.0.193
- Fixed a bug where the query editor raised errors on some syntaxes, including delimited numeric literals.

# 1.0.192
- Added the configuration "sqlite3-editor.ui.mergeIdenticalCells".
- Fixed a bug introduced in the previous version, which prevented rendering foreign key values in cells.

# 1.0.191
- Added support for placeholders in the query editor.

# 1.0.190
- Updated the bundled SQLite to version 3.46.1.
- Improved the UI for hiding columns.

# 1.0.189
- Improved the user experience of the foreign key dropdown.
- Added a list to pick values for column filters.
- Improved the query editor to ignore dot commands on Shift+Enter.
- Improved the "Export / Import" feature to open a file dialog.
- Improved the "Export to XLSX" and "Open in Excel" features to format cells as Excel tables, and added the option to export all tables.

# 1.0.188
- Updated the bundled SQLite to version 3.46.0.

# 1.0.187
- Fixed overflow of placeholders in text areas.
- Fixed the error "TypeError: Do not know how to serialize a BigInt".
- Potentially fixed the error "load command 0x80000034 is unknown" on Darwin 17.
- Fixed the SQL parser to properly parse table names that are non-quoted SQL keywords.
- Made the editor remember the its state until closing the VSCode window.
- Made the editor exit [preview mode](https://code.visualstudio.com/docs/getstarted/userinterface#_preview-mode) when clicked.

# 1.0.186
- Updated the bundled SQLite to version 3.45.3.

# 1.0.185
- Resolved `Error: prefetched table list was used twice`.

# 1.0.184
- Updated the documentation.

# 1.0.183
- Updated the bundled SQLite to version 3.45.2.
- Fixed the compatibility issue for Windows 7 (#50).
- Updated the textarea to respect some of the VSCode configurations under "editor.*".

# 1.0.182
- Fixed the scroll amount of the arrow left and arrow right keys on the table.
- Fixed the STATUS_ENTRYPOINT_NOT_FOUND error on Windows 7 (#50).

# 1.0.181
- Improved error handling.
- Added a button to temporarily enable editing in virtual workspaces and removed the "dangerouslyWriteToVirtualWorkspaces" configuration option.

# 1.0.180
- Added the feature to write comments on tables.
- Corrected the error message for when an executable file is missing (#48).
- Updated the textarea to be resizable by dragging on its bottom edge, not just on its bottom right corner.
- Fixed several minor bugs.

# 1.0.179
- Disabled write operations on virtual workspaces because they have a risk of corrupting the database.

# 1.0.178
- Added support for editing and dropping broken views.
- Added the feature to select multiple tables in the table selector with Alt+Click or Shift+Click.
- Added the feature to display columns and values of a table with Ctrl+Click.
- Improved the rename view feature to allow editing the view's name on the table selector dropdown.
- Added support for autocompletion and documentation hover for functions added by SQLite runtime loadable extensions. Note that all function names are lowercased because SQLite lowercases function names internally.
- Fixed bugs in rendering of foreign key values in cells.

# 1.0.176
- Fixed regressions in the key combination labels for Mac, the click event handler on the blank area of the table, and the Ctrl + ArrowLeft/ArrowRight shortcuts on cells.
- Added the "Copy All Column Names" context menu item to the table header.

# 1.0.175
- Fixed a bug in the parser for CREATE VIEW statements that resulted in incorrect rendering of relationships in the ERD.

# 1.0.174
- Fixed bugs related to virtual tables.
- The ERD now displays the relationship between FTS virtual tables and their content tables.
- Added the configuration "sqlite3-editor.ui.tableSelector.displayShadowTables" with a default value of false.
- Fixed several other minor issues reported by users.

# 1.0.173
## Improvements
- Added the option "sqlite3-editor.ui.minimizePanel" which minimizes the bottom panel.
- Improved rendering performance for wide tables by rendering only visible columns. Removed the "sqlite3-editor.ui.visibleColumnLimit" option, as it is no longer needed to prevent freezing the window on wide tables.
- Added the configuration "sqlite3-editor.ui.commitOnEnterOrTab" which allows editing cells with a single press of the Enter key, rather than twice.
- Updated to save textarea heights until the editor tab is closed.
- Increased margins in the UI. You can adjust them with the configuration "sqlite3-editor.ui.spacing".
- Added the shortcut Shift+Alt+N for 'NULL' in UPDATE statement editor.
- Enhanced auto-completions for PRAGMA statements.
- Improved the style of switches used to toggle column visibility.
- Updated charts plotted by the 'Plot' feature to prevent them from going outside of the window.
- Optimized rendering performance for conditional formatting.
- Added a button to send feedback in the 'Other Tools...' menu for users who have provided feedback via the dialog shown after using this extension for some time.
- Dropped the configuration "sqlite3-editor.ui.nativeTableSelector", which has been deprecated since 1.0.148.

## Bug Fixes
- Fixed the error "Reduce of empty array with no initial value".
- Fixed the error "Unable to preload CSS for...".

# 1.0.172
- Further optimized the loading speed of the editor.
- Fixed several minor issues reported by users.

# 1.0.171
- Optimized the editor's loading speed.
- Switched to using backticks (\`\`) instead of double quotations ("") for escaping identifiers in SQL queries to fix a bug where identifiers were misinterpreted as string literals if the identifiers did not exist.
- Fixed several other bugs.

# 1.0.169
- Fixed the condition for displaying the confirmation dialog that prevents losing user input.

# 1.0.168
- Added the feature to find foreign key references to a value. [#35](https://github.com/yy0931/sqlite3-editor/issues/35)
- Added the feature to open a table in a new tab through the context menu or by middle-clicking on the table selector.

# 1.0.167
- Fixed the "Unexpected end of MessagePack data" error.
- Added error handling for STATUS_DLL_INIT_FAILED.
- Improved the style of the separator in the "Group by Value" feature.
- Updated the bundled SQLite to version 3.45.1.

# 1.0.165
- Fixed a bug introduced in version 1.0.163 where the foreign key dropdown was always hidden.

# 1.0.164
- Increased the minimum required VSCode version to 1.70 and resolved issues affecting earlier versions of VSCode.

# 1.0.163
- Added support for canceling long-running queries via a notification button. [#46](https://github.com/yy0931/sqlite3-editor/issues/46)
- Added the feature to filter columns with arbitrary SQL expressions. [#47](https://github.com/yy0931/sqlite3-editor/issues/47)
- Expanded the undo feature to include more actions.
- Possibly fixed the "Unexpected end of MessagePack data" error.
- Fixed the BulkInsert's Ctrl+V shortcut to display the confirmation dialog when the editor is dirty.
- Addressed other minor issues.

# 1.0.162
- Updated the bundled SQLite to version 3.45.0.
- Fixed the parsing of "WITH ... INSERT/DELETE/UPDATE ..." statements. [#45](https://github.com/yy0931/sqlite3-editor/issues/45)
- Added a progress bar for long running queries in the query editor. [#46](https://github.com/yy0931/sqlite3-editor/issues/46)
- Added the "Use SQL Expression" option for column filters.

# 1.0.161
- Fixed several user-reported runtime errors.

# 1.0.159
- Fixed some issues in the foreign key dropdown.
- Improved the rendering performance of tables containing foreign keys.
- Updated the style of the horizontal scrollbar on the table to match the vertical one.
- Added the configuration "sqlite3-editor.ui.tableCellForeignKeyPreview.opacity".

# 1.0.158
- Added experimental undo and redo functionality.
- Fixed several user-reported issues in the ERD feature.

# 1.0.156
- Improved the performance of the foreign key dropdown for large number of options.
- Improved the table cell to render foreign key values.
- Added a button next to the foreign key dropdown to open the source table.
- Added the Ctrl+L shortcut to open the table selector.
- Added support for REFERENCES in the CREATE TABLE editor.
- Updated context menus to respond to keyboard events.
- Fixed a bug where dropping all tables from a database displayed an error message.

# 1.0.155
- Reversed the arrows in entity-relationship diagrams to match convention.

# 1.0.153
- Fixed a bug where some keybindings could be triggered within a composition session.
- Added support for JSONB.
- Added the "Use the first row as a header" option to the bulk insert feature.
- Added the dropdown to select a CSV delimiter to the bulk insert feature.
- Added the feature to display entity-relationship diagrams. It is available in the table selector when the database includes foreign keys or views.
- Fixed another bug that caused "Query returned no rows" error, in addition to the one fixed in v1.0.152.
- Slightly improved the extension's startup time.

# 1.0.152
- Added auto-completion and syntax checking to the embedded text editors.
- Fixed the "Query returned no rows" error.
- Fixed a bug where generated columns could not be edited.
- Updated the bundled SQLite to version 3.44.2.

# 1.0.151
- Updated the text selection color.

# 1.0.150
- Fixed a bug in the foreign key dropdown. [#41](https://github.com/yy0931/sqlite3-editor/issues/41)

# 1.0.149
- Fixed the load error on offline environments. [#40](https://github.com/yy0931/sqlite3-editor/issues/40)
- Added support for inserting records over views and queries.
- Improved the performance and styling of the table selector dropdown.
- Added the configuration "sqlite3-editor.ui.tableSelector.displayColumns", which shows the table columns in the table selector dropdown.
- Removed invisible backdrops from the context menu.
- Added support for in-place editing of table names.
- Improved the algorithm for the auto-reload feature to minimize its latency.
- Added "Export Table to Excel" to the "Other Tools" menu.
- Fixed the issue where triggers on views were not listed in the schema pane.
- Fixed the issue where pressing Ctrl+Enter when a confirmation dialog was shown committed the changes but left the dialog open.
- Fixed the bug in the range selection feature on read-only editors.

# 1.0.147
- Improved the design of the context menu and font choices.
- Enhanced performance for deleting multiple records.
- Added partial support for deleting rows through a query. Rows can now be deleted by dragging on row numbers. Deleting rows via the context menu on a range selection of cells is not yet supported.

# 1.0.145
- Fixed an issue where the extension did not respond to scrolling while dragging.
- Added the feature to rename triggers.

# 1.0.142
- Added the feature to rename indexes.
- Added the feature to generate a template for a CREATE TRIGGER statement.
- Added auto-completion for NEW and OLD in the query editor.
- Added support for range selection on WITHOUT ROWID tables.
- Added the context menu button "Delete Rows" for range selections on tables with ROWID.
- Improved the styling of the row resizer, schema pane, table header, etc.
- Fixed many other bugs.

# 1.0.140
## Improvements
- Added the configuration "sqlite3-editor.ui.tableHeaderMaxLines".
  - The configuration "sqlite3-editor.ui.wrapTableHeader" is deprecated. Please use `"sqlite3-editor.ui.tableHeaderMaxLines": 1` instead.
- Added the feature to change the height of table rows. To use this, simply drag the bottom of a row number.
- Added the feature to filter records based on a specific value in the chosen column. To use this, right-click on a table column header. Alternatively, you can also set a filter via the context menu on cells.
- Added Shift+Up/Down/PageUp/PageDown shortcuts for expanding row selections.
- Updated the renderer for the table column header to display UNIQUE constraints, multi-column PRIMARY KEYs, and INDEXes.
- Added a context menu for row selections.
- Added the "Open in Excel" button to the "Other Tools" menu on Windows.
- Added the feature to visualize indexes to the "Schema" pane.
  - The configuration "sqlite3-editor.ui.indexVisualization.maxColumns" controls the limit on the number of columns.

## Bug Fixes
- Fixed several bugs in the "Group by Column" feature.
- Fixed the issue where the extension did not activate on codespaces and code-server. [#37](https://github.com/yy0931/sqlite3-editor/issues/37)
- Fixed a bug where closing a VSCode window deletes the cache used by the extension's instance in another VSCode window, resulting in `UNKNOWN: unknown error, open ...-shm errno: -4094`. (#30)

# 1.0.136
- The extension now respects VSCode's color theme and uses colors from it.

# 1.0.135
- Improved error handling.
- Enhanced performance of the dropdown for foreign key columns.
- Fixed a bug where the "auto-fit width" feature didn't function when conditional formatting was applied.
- Updated the confirmation dialog to display the query about to be executed.
- Made the plotting feature available without an experimental flag.

# 1.0.132
- Added tutorial popups for new users on how to use certain buttons.
- Updated the style of the switch that specifies data types.
- Updated the "Edit Table Schema" feature to allow dropping all existing columns.
- Fixed the condition for displaying the "There are no tables in the database." message.

# 1.0.131
- Maybe fixed a rendering bug of the UPDATE panel, although I could not reliably reproduce the bug.
- Updated the styles of several components in the UI.

# 1.0.130
- Fixed a rendering issue where row numbers were rendered below table cells.

# 1.0.129
- Updated the styles of several components in the UI to look more modern.

# 1.0.128
- Implemented auto-fills for the INSERT editor.
- Made the editor to restore table state (sort, group by, scroll position, etc.) when switching back to a table that was active in the same connection.
- Added a feature that allows queries to be pinned as inner-view tabs. This can be enabled through the `sqlite3-editor.ui.alwaysDisplayTabs` setting.
- Added buttons that allow moving the bottom panel to the left or right when there is extra space beside the table.
- Added context menus to the group headers of the Group by Column feature.
- Added the configurations `"sqlite3-editor.insertHelpComment"`, which can be used to hide the default comment in the query editor.

# 1.0.125
- Fixed bugs in the Find feature.
- 
# 1.0.124
- Fixed a bug in the auto reloading feature on Linux and Mac.
- Added the feature to specify which columns the find widget should search.

# 1.0.123
- Implemented context-aware auto completions for the query editor.

# 1.0.121
- Updated the feature documentation.
- Fixed a bug in the auto reloading feature.

# 1.0.120
- Aligned the positions of context menus displayed on a left mouse button click.
- Added support for PRAGMA statements with parentheses in the query editor.
- Added the feature to edit GENERATED columns like other columns.
- Improved the intuitiveness of the UI for the ADD COLUMN feature.
- Fixed bugs that sometimes caused context menus to render partially.

# 1.0.119
- Added the shortcut Alt+Click for "Group by Column".

# 1.0.118
- In previous versions, if a SELECT statement executed from a query editor was present, the "Query Editor" button unset it rather than opening a new editor, which was confusing. From this version, the button always opens a new editor. To unset a SELECT statement, click the SELECT statement.
- Fixed the condition that displays the performance notice (`sqlite3-editor.ui.performanceNotice`).

# 1.0.117
- Added a cache for slow SELECTs to make scrolling faster. The cache uses up to 64MiB of RAM.

# 1.0.114
- Improved the design of the group separators in the "Group by Column" feature.
- Fixed a bug where range selections were not working on grouped tables.

# 1.0.113
- Added the "Group by Column" feature.
- Added a help message to the error `foreign key mismatch - `.
- Added the configuration `sqlite3-editor.pragma_foreign_key`.
- Fixed the bug that occurred when renaming a table using the "edit table schema" feature.

# 1.0.112
- Optimized the rendering speed of conditional formatting.
- Fixed the handling of PRAGMA in the query editor.
- Improved the UI for hiding columns.
- Made the SQLite version label open SQLite documentation when clicked.
- Added XML support to the textarea.
- Upgraded the bundled SQLite to 3.43.1.
- Added the `sqlite3-editor.ui.visibleColumnLimit` and `sqlite3-editor.ui.insert.textareaLimit` configurations to prevent VSCode from freezing when opening large tables.

# 1.0.110
- Fixed `Process exited: 3221225781` on Windows.

# 1.0.108
- Fixed the issue where the "update over views or queries" feature was not working on tables that have a "INTEGER PRIMARY KEY" column.

# 1.0.105
- Added configurations `sqlite3-editor.codeLens.hideExecuteAndSelectButtons` and `sqlite3-editor.diagnostics.disableSyntaxCheck`.
- Added translations.

# 1.0.103
- Updated the README.

# 1.0.102
- The foreign key dropdowns now render the values in the referenced records.

# 1.0.101
## Improvements to Foreign Key Dropdowns
- Made the feature available without an experimental flag.
- Added support for indirect foreign keys (views and queries that reference FOREIGN KEY columns).
- Added the configuration option `sqlite3-editor.ui.foreignKeyDropdownLimit`.
- Improved the style.

## Other Changes
- Improved the response time for the Enter and Tab keys in cells by making the retrieval of record counts asynchronous.
- Updated the table to allow horizontal scrolling with shift + wheel.
- Resolved the issue where the "Edit View" and "Rename View" features were dropping triggers.
- Added the guide on INSTEAD OF INSERT triggers.

# 1.0.99
- Added an experimental feature `sqlite3-editor.ui.experimental.foreignKeyDropdown`.

# 1.0.98
- Upgraded the bundled SQLite to 3.43.0.
- Fixed the handling of PRAGMAs in the query editor.

# 1.0.97
- Improved handling of invalid UTF-8 strings.

# 1.0.96
- Lowered minimum required glibc version for x86 and arm64 to glibc 2.17.
- Added conditional formatting feature.

# 1.0.94
- Fixed the handling of failed transactions.
- Fixed other bugs introduced in v1.0.91.

# 1.0.91
- This extension no longer requires Python. We've rewritten all Python scripts in Rust and included the compiled executables for win32-{ia32,x64,arm64}, darwin-{x64,arm64}, and linux-{x64-{gnu,musl}, arm64-{gnu,musl}, armhf-gnu} in the extension. The optional component `column_origin.c` that required users to install a C compiler has also been ported to Rust.
- Updated the textareas to use the same text editor implementation as VSCode.
- Added a editor title button (the buttons placed at the top right corner of the editor) to connect to a database for .sql files.
- Added the "Rename View" editor.
- Fixed an issue that was causing separate in-memory databases to be created in the query editor and the extension's panel when connecting to an in-memory database via code lens in .sql files.
- Fixed an issue where table cells sometimes did not take focus when clicked.
- Added the "Execute Selection" command to the query editor. It can be called from the command palette or context menu.
- We have dropped the experimental support for DuckDB. This feature had very low usage (only 0.4% of users tried it according to our opt-in telemetry) yet had significant maintenance costs due to DuckDB's wide range of features. If you were using this feature, we recommend migrating to [DuckDB Driver for SQLTools](https://marketplace.visualstudio.com/items?itemName=Evidence.sqltools-duckdb-driver) or [DuckDB Sql Tools](https://marketplace.visualstudio.com/items?itemName=RandomFractalsInc.duckdb-sql-tools).

# 1.0.90
- Resolved the "python.exe: No module named server_py" error that occurred when [the embeddable package](https://docs.python.org/3/using/windows.html#the-embeddable-package) was used.

# 1.0.89
- Redesigned the UI placements.
- Optimized the rendering performance.
- Improved the error handling.

# 1.0.86
- Added the configurations `ui.alignNumberRight`, `ui.defaultIndexName.*`, `ui.wrapTableHeader` and `ui.recordCountingLimit`.
- Enhanced data loading UX:
  - Added a loading spinner.
  - Added a status bar item displaying the currently executed query.
- Enhanced features for table schema editing:
  - Added a feature to modify the table schema, accessible through `Schema` > `Edit`.
  - Added a feature to modify column definitions, accessed by Ctrl+Click on column headers.
  - Added the Ctrl+Click shortcut and in-place editing for `ALTER TABLE RENAME COLUMN` on column headers.
- Enhanced UX for data copying:
  - Table cells now have distinct background colors in focused and unfocused states to indicate which data will be copied when `Ctrl+C` is pressed.
  - `Ctrl+C` is now supported in row selections (the `DELETE` state).
  - Added an indicator shown during data copying.
- Optimized rendering performance and memory usage.
- Added new features:
  - Added the "Open in Command Line Shell" context menu item, displayed only if `sqlite3` or `sqlite3.exe` is in PATH.
  - Added the "Bulk INSERT" feature.
  - Added a context menu item to add an index to the table header.
  - Added a status bar item showing the record count.
- Made other UX improvements:
  - Updated the font color of the `-- database: ...` line in query editors.
  - The table no longer auto-scrolls to bottom upon record insertion when data is sorted.
  - Moved the "duplicate table" context menu item from the "other tools" button to the table selector.
  - Made the insertion and update editors more compact on wider displays.
  - Improved the UX of row deletion. [#18](https://github.com/yy0931/sqlite3-editor/issues/18)
  - Added tooltips.
- Fixed bugs:
  - Fixed the CSV export feature. [#22](https://github.com/yy0931/sqlite3-editor/issues/22)
  - Fixed the issue where the "Delete..." context menu item for row numbers on WITHOUT ROWID tables wasn't working.
  - Improved the error handling for the `no such table` issue. [#21](https://github.com/yy0931/sqlite3-editor/issues/21)

# 1.0.85
- Improved the error handling of spawning Python.

# 1.0.84
- Fixed the "Connect" button that was not responding.
- Excluded "ISNULL" from auto-completion.
- Improved the style of the contextmenu in the table header.
- Added a "+" button to add a column to the table header.
- Added a feature to reorder columns, as was requested through feedback.
- Improved the table header label to display HIDDEN, VIRTUAL, and STORED keywords.
- Added the `Go to Table/Row` (Ctrl + G) command.
- Changed the button label in the context menu that was shown on right clicking the table name.
- Removed the Ctrl(Cmd) + Shift + Q keybinding. You can revert this change by adding the following entry to your `keybindings.json`.
  ```json
  {
    "key": "ctrl+shift+q",
    "mac": "cmd+shift+q",
    "command": "sqlite3-editor.execute",
    "when": "editorLangId == query-editor"
  },
  ```

# 1.0.80
- Changed the order of table names to table, view, virtual, and shadow.
- Added a notification to explain --tsv and --delimiter options in the CSV import feature [#19](https://github.com/yy0931/sqlite3-editor/issues/19)

# 1.0.79
- Fixed the error messages for ALTER TABLE.
- Improved the visibility of the flashing effect.
- (v1.0.79) Fixed a minor bug introduced in v1.0.78.

# 1.0.77
- Changed the storage location for temporary files to resolve the `ENOSPC: no space left on device, open '/tmp/...` issue.

# 1.0.76
- Fixed the behavior of scrollbar and a translation.
- Changed the text color of `""` in the query editor.

# 1.0.75
- Fixed the dark theme.

# 1.0.74
- Fixed an issue where column widths were stored as bigint, causing the error `Cannot mix BigInt and other types, use explicit conversions` and preventing the find widget from being displayed. [#16](https://github.com/yy0931/sqlite3-editor/issues/16)
- Added a color to the row on the selected cell. [#16](https://github.com/yy0931/sqlite3-editor/issues/16)

# 1.0.73
- Added feature to open links with Ctrl+click or context menu item. [#16](https://github.com/yy0931/sqlite3-editor/issues/16)
- Fixed several reported bugs, including:
  - `RangeError: Invalid count value`
  - `[UriError]: If a URI contains an authority component, then the path component must either be empty or begin with a slash ("/") character`
- Changed keyboard shortcuts on Mac to use Cmd instead of Ctrl.

# 1.0.72
- Fixed several bugs reported.

# 1.0.71
- Addressed a bug where a GitHub button was not responding.

# 1.0.70
- Updated translations.

# 1.0.69
- Resolved an issue where Python binaries that were installed from Microsoft Store could not be found.
- Added a button "Connect" along with "Connect and Open Panel" in the query editor.
- Updated the query editor to send SELECT statements to the last selected webview.
- Added a configuration `completion.functionCase`.
- Added a command palette entry `sqlite3-editor.openInMemoryDatabase`.
- Added translations for de, es, fr, it, ja, ko, pt-BR, ru, zh-CN, and zh-TW, and a form to report translation errors.
- Edited the labels on buttons for clarity.
- Added completion items.

# 1.0.68
The following changes have been made in this update:

## Diff Editor
You can now view side-by-side comparisons of two database versions in the source control view. To see the differences between the versions, click "Compare database with local file." Keep in mind that large databases may take longer to display differences, and if locking databases is an issue for your use-case, it's better to avoid using this feature.

## Other Changes
- Added a button to copy text to the GUI editor for UPDATE statements.
- Tables now use oid or _rowid_ for sorting records if rowid column is overridden.

## Bug Fixes
- Fixed runtime errors on read-only virtual workspaces.
- Fixed a bug where the find widget loses focus when the selected cell was redisplayed.
- Fixed a bug in the SQL parser for the custom query editor where ATTACH DATABASE and DETACH DATABASE were not being recognized as SQL statements.
- Fixed a bug where column widths were not being saved properly.
- Fixed a bug that caused error messages to be rendered twice in webviews.
- Fixed bugs in the "show journal mode" and "show synchronous flag" in the "other tools..." menu.
- Fixed "Webview is disposed" errors.
- Fixed a shell escaping issue: https://github.com/yy0931/sqlite3-editor/issues/14

# 1.0.67
The following changes have been made in this update:

## Document Formatter
You can now format queries by selecting "Format Document" in the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) or by pressing Shift+Alt+F.\
This feature uses [sql-formatter](https://github.com/sql-formatter-org/sql-formatter) to format queries.

## Buttons to Select CTEs
To make it easier to create a complex query involving [CTEs](https://www.sqlite.org/lang_with.html), we have added buttons that enable you to display the output of each CTE.

## Syntax Validator
We have added a syntax validator to the query editor. To achieve this, we [prepare](https://www.sqlite.org/c3ref/prepare.html) (or compile) each statement in the editor and check for syntax errors. However, some PRAGMAs does their work when the statement is prepared [1], so we do not check them for syntax errors.

[1] "Some PRAGMA statements do ..." in https://www.sqlite.org/lang_explain.html#explain_operates_at_run_time_not_at_prepare_time

## Other Changes
- We added left padding to row numbers to ensure the row number column has the same width regardless of the scroll position.
- We added a button "Reset Column Width" to the table header.
- We fixed a bug where [generated columns](https://www.sqlite.org/gencol.html) were not displayed.
- We fixed the hover provider for the query editor.


# 1.0.66
The following changes have been made in this update:

## Displaying and Jumping to the Definition of Foreign Keys
We have added a new feature that allows users to display and jump to the definition of foreign keys by using mouse hover and context menus.

## "Autofit Column Width" Button
To help users adjust column width quickly, we have added the "Autofit Column Width" button to the table header.

## Additional Auto Completion Items
We are gradually introducing new auto completion items with each release. In this update, we have included completion for IF NOT EXISTS, AUTOINCREMENT, STRICT, and more.

## Other Changes
- Fixed a bug where `VACUUM;` was not recognized as a statement in the query editor.
- Added icons to the context menu.
- Changed the default data type for inserting values into AUTOINCREMENT columns from NUMERIC to DEFAULT.


# 1.0.65
- Updated the container for error messages so that it is scrollable.
- Fixed a bug where setup queries specified in `sqlite3-editor.connectionSetupQueries.driver.sqlite3` were not executed for some connections.
- Added the `sqlite3-editor.runtimeLoadableExtensions.driver.sqlite3` configuration.
- Translated the dialog added in v1.0.60.
- Updated the documentations in the README.

# 1.0.64
- Moved the dialog added in v1.0.60 into the webview.

# 1.0.63
- Added a `create database` button to the webview that is shown when the database specified in `-- database:` does not exist.
- Fixed the error handling of file accesses.
- Fixed the condition to show the dialog added in v1.0.60.

# 1.0.62
- Fixed badges in the README.

# 1.0.61
- Optimized the UI's rendering.
- Parallelized the startup code.
- Fixed a caching issue for DuckDB during startup.
- Added a read-only text area for UPDATEs on views and custom queries.
- Added a ▷ button to the query editor and removed the `Ctrl+Shift+E` shortcut as it was conflicted with `View: Show Explorer`.
- Fixed a bug where ctrl+Enter does not functioning when `sqlite3-editor.nativeTableSelector` was set to true and the table name was focused.
- Updated the README and telemetry.

# 1.0.60
- Added a dialog to request users to give a star to the repository. If you have already done so, thank you!

# 1.0.59
- Added a survey (a Google Form) for new users.
- Updated the README.

# 1.0.58
- Updated the auto reloading feature to watch duckdb's .wal file.

# 1.0.57
- Fixed an issue where statements with multiple semicolons, such as create trigger, could not be executed in the query editor.

# 1.0.56
- Fixed `cannot commit transaction - SQL statements in progress` on INSERT

# 1.0.55
- Added the `sqlite3-editor.nativeTableSelector` configuration option to change the UI for selecting tables, with the older UI set as the default. (#11)

# 1.0.54
- Fixed bugs around editors duplicated by `View: Split Editor`.
- Added NaN check for number inputs.
- Changed the tree view to highlight the active table name.
- Added a check for file magics and file permissions.
- Fixed errors for empty files with the extension `.duckdb`.
- Added a tooltip to `AS DEFAULT`.
- Removed the "Execute SQL" button in the context menu on the editor's statement as it had the same functionality as the "Custom Query" button.

# 1.0.53
- Table selection now uses VSCode's native quick pick. This improves performance when the number of tables is large (> 1000), and also enables fuzzy matches.
- Added a view for listing tables to the explorer. It should be useful for quickly switching between tables.
- Added the following commands. They are displayed in the command palette only when a SQLite editor or its query editor is active.
  - `SQLite3 Editor: Toggle Table Schema Visibility`
  - `SQLite3 Editor: Open Custom Query Editor`
  - `SQLite3 Editor: Toggle Auto Reload`
  - `SQLite3 Editor: Find`
  - `SQLite3 Editor: Select Table`

# 1.0.52
- Resolved the error "Illegal argument: character must be non-negative" displayed in the query editor.

# 1.0.51
- Added `sqlite3-editor.connectionSetupQueries.*` options.
- Changed the style sheet to use the font specified with `editor.fontFamily` in the webview. (#9)
- Fixed a bug in the parser for table schemas where tables with a WITHOUT ROWID option and newline characters in their schema could not be opened using SQLite <3.37. (#10)

# 1.0.50
- Added error messages for unsupported table types.
- Updated the README.

# 1.0.49
- Added a close button to the find widget.
- Fixed the style sheet for the table listing pythons found.
- Fixed runtime errors on arrow keys when cell outside view is selected.
- Added keybindings for arrow keys when selecting multiple cells.
- Fixed an issue where hiding columns breaks the rendering of the rightmost column.
- Changed the editor below the table to not clear data on error.
- Fixed a bug where a dragging starts when closing a dialog.
- Changed the style sheet to highlight row numbers of cells selected.
- Added telemetry. Read the README for information.

# 1.0.48
- Decreased the priority of the extension's language mode. (#8)
- Added a feature to select multiple cells.

# 1.0.47
- Improved the startup performance.
- Added a diagnostic provider for "DELETE * FROM".

# 1.0.46
- Updated the README.
- Fixed the script to generate documentations shown in hovers.

# 1.0.45
- Fixed an issue where the hover on table names in query editors was sometimes not displayed.

# 1.0.44
- Fixed the runtime error "Process exited: 2 usage: py ..." on systems with pythonpy installed.

# 1.0.43
- Enhanced the query editor's user experience by
  - Changing the behavior of Shift+Enter to execute the statement on the cursor, rather than the entire file.
  - Determining whether to set the query for the table or not by checking if the statement is a SELECT statement.
  - Displaying buttons to execute each line in the editor.
  - Escaping column and table names in autocompletion items if needed.

# 1.0.42
- Updated the completion provider for the query editor to provide combinations of keywords.
- Fixed the handling of mouse events on the scrollbar and the preview button on BLOB columns.
- Fixed a runtime error when using duckdb.

# 1.0.41
- Fixed a runtime error on tables with `REFERENCES` that do not have an explicit parent key.

# 1.0.40
- Added a notification that is displayed after a successful execution of Ctrl+Shift+E (sqlite3-editor.executescript).
- Added a context menu for the table header to enable previewing BLOB values in non-BLOB columns.
- Added partial support for non-utf-8 TEXT values.
- Fixed an issue where a "webview is disposed" notification was sometimes displayed when closing an editor.
- Fixed a bug that prevented opening database files in network-mounted drives.
- Added buttons to report errors.

# 1.0.39
- Changed the UI to be less blue in dark mode.
- Fixed a bug where foreign keys with different referencing and referenced names were not displayed in the table header.
- Added context menu buttons ("open referenced columns" on the table header and "open in query editor" on the commit button).
- Reversed the direction of arrows for ORDER BY.
- Improved the response time of autocompletion by deduplicating completion items.

# 1.0.38
- Improved the algorithm for searching Python binaries.
  - The extension now selects the Python version with the latest database engine.
  - Fixed a bug where Python binaries with name python3.6, python3.7, etc. could not be found.
  - You can now check the list of Python binaries found by hovering over the version string at the top right corner.
- Added SQLite version checks and warning messages.
- Updated exporting of JSON/CSV to take into account hidden columns and custom queries.

# 1.0.37
- Fixed file descriptor leaks on error handling.
- Added support for SQLite compiled without the SQLITE_ENABLE_UPDATE_DELETE_LIMIT option.

# 1.0.36
- Fixed a runtime error on Python 3.11+ (#4)

# 1.0.35
- Adjusted the background color of selected cells.
- Changed the position of the find widget when the number of columns is small.
- Fixed a bug where regex searches did not match numbers.

# 1.0.34
- Reduced the minimum required version of VSCode from 1.71.0 to 1.66.0, which is the earliest version of VSCode that runs Node.js 16.x.
- Added a feature to highlight cells that have the same value as the selected cell.
- Added a default shortcut `Shift+Enter` for `sqlite3-editor.query` because `Cmd+Shift+Q` was already bound for quitting the application on Mac.
- Fixed a rendering issue when the screen width is narrow.

# 1.0.33
- Added "Show Synchronous Flag", "Set Synchronous Flag…", and "Optimize" buttons in the Other Tools menu.
- Fixed an animation bug.

# 1.0.32
- Fixed a bug that was implicitly casting rounded floating values to integers.
- Fixed bugs related to key bindings and rendering of table cells.

# 1.0.31
- Fixed a rendering bug of table cells.
- Fixed a bug that caused table cells with null values to be uneditable.

# 1.0.30
- Moved the small buttons to switch editors to the context menu on the editor's header.
- Added a feature to select multiple records by alt+click.
- Updated the style of the table schema viewer, and updated it to display triggers.

# 1.0.29
- Added a feature to sort columns by clicking column headers.
- Dropped the plain textarea-based editors for custom queries.
- Added the "Unhide all columns" context menu button to the table header.

# 1.0.28
- Improved performance when scrolling.
- Added support for scrolling when opening the UPDATE or DELETE editor.

# 1.0.27
- Added a feature to edit data through a view or a custom query.

# 1.0.26
- Added support for virtual workspaces (#3)
- Added a feature to edit custom queries in another VSCode's tab, a similar feature to alexcvzz's SQLite extension. It supports syntax highlighting, code completion, hover, and signature provider.
- Fixed the command that is displayed in the git-diff view.
- Fixed a bug that caused runtime errors when using an older version of sqlite.
- Increased the maximum number of characters that can be displayed in a cell.

# 1.0.23
- Made the textarea for custom SELECT statements full width and resizable.

# 1.0.22
- Added a feature to show history in the "Execute SQL" editor.
- Fixed a runtime error that occurred when opening databases with views.
- Added context menus to copy the SELECT statement.

# 1.0.21
- Fixed a bug that caused runtime errors when opening databases containing views.

# 1.0.20
- Added an optional editor for `Open With…`.

# 1.0.19
- Updated the UI.
  - Render the table in full width.
  - Prevent the scrollbar of the webview and the scrollbar of the table from overlapping.
  - Scroll the table when ArrowLeft or ArrowRight keys are pressed.
  - Preview image, video, and sound files embedded in BLOB columns.
  - Fix a positioning issue of the context menu at the edge of the window.
- Fixed an issue where the custom query editor didn't run multiple SQL statements.
- Added experimental support for DuckDB. Many features have not yet been implemented.
- Added an icon and a demo video.

# 1.0.18
- Added context menu items.
- Fixed the behaviors of keyboard shortcuts around hidden columns and BLOB columns.
- Changed the BLOB editor to use file pickers to select filepaths instead of a textarea.
- Fixed a bug that caused the switches for the data types in the INSERT editor to be ignored in the resulting SQL query.

# 1.0.17
- Fixed a bug where the terminal opened by the Tools button would not reopen after being closed.

# 1.0.16
- Added an integration with sqlite-utils, which can be accessed via the Tools button.
- Fixed an issue where [SQLite's temporary files](https://www.sqlite.org/tempfiles.html) were not being deleted after the editor was closed, due to the connection to the database not being closed properly.
- Fixed an issue where auto-reloading was not functioning for databases that had WAL mode enabled.

# 1.0.15
- Reduced the minimum required version of SQLite bundled with Python from 3.37.0 to 3.8.7.1 by adding fallback code for `PRAGMA table_list` using `sqlite_master`.

# 1.0.14
- Fixed [#2](https://github.com/yy0931/sqlite3-editor/issues/2): Added a check to see if the version of SQLite bundled with Python meets requirements.
- Fixed an issue where Python binaries installed from Microsoft Store could not be found.

# 1.0.13
- Fixed an issue where certain characters had insufficient contrast in the dark theme, making them difficult to read.
- Fixed an issue where high-contrast-light themes were classified as dark themes.
- Improved error handling for when spawning Python fails.
- Fixed an issue where the animation triggered by clicks was not playing on slow machines due to a timing issue.

# 1.0.12
- Added support for dark themes.

# 1.0.11
- Added the ability to hide columns.
- Added context menus to the table header and row numbers.
- Fixed an issue where the editor state was reset without prompting the user when using an editor other than UPDATE and clicking the right side of the table.
- Improved error handling for when the Python binary specified in the settings.json does not exist.
- Added `ORDER BY rowid` to SELECT queries.

# 1.0.10
- Fixed a bug that caused the default table height to be set to 200 instead of 20. The bug was due to the misconception that `{a: 1, ...{a: undefined}}` would output `{a: 1}`.

# 1.0.9
- Fixed an issue of stuttering when changing the table's height.
- Fixed a bug where the input box in a cell would not respond to mouse clicks.

# 1.0.8
- Improved the error handling of the extension. The extension now displays runtime errors raised by Python in popups.

# 1.0.7
- Fixed runtime errors with Python versions lower than 3.8.3.

# 1.0.6
- The extension now displays blank rows when there are few records, and switches to the INSERT editor when one of the cells is clicked.
- The "Commit changes?" dialog is now displayed for the INSERT, CREATE TABLE, CREATE INDEX, and custom query editor, as well as the UPDATE editor.
- Tooltips on icon buttons are now displayed immediately when hovered, to improve accessibility.

# 1.0.5
- Fixed a bug where columns could not be resized while a cell is selected.
- Added a cancel button to the "Commit changes?" dialog.
- Made the "Commit" button the default focus in the "Commit changes?" dialog.
- Fixed the behaviors of the Enter and Tab keys while editing a cell.
- Added `LICENSE` (MIT) and `vendor.LICENSE.txt`.

# 1.0.4
- Fixed an issue where undo/redo were not working on textareas due to preventDefault() being called by VSCode.

# 1.0.3
- Fixed [#1](https://github.com/yy0931/sqlite3-editor/issues/1): *.sqlite and *.sqlite3 are now recognized as SQLite databases.

# 1.0.2
- Fixed a bug introduced in v1.0.1.

# 1.0.1
- Added keyboard shortcuts to move a selection in the table.
