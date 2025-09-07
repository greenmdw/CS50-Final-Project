# SQLite3 Editor

[![Github Stars](https://img.shields.io/github/stars/yy0931/sqlite3-editor?style=social)](https://github.com/yy0931/sqlite3-editor)
[![GitHub issues](https://img.shields.io/github/issues/yy0931/sqlite3-editor)](https://github.com/yy0931/sqlite3-editor/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/yy0931/sqlite3-editor)](https://github.com/yy0931/sqlite3-editor/issues)

This extension allows you to edit [SQLite 3](https://www.sqlite.org/index.html) files without having to write SQL queries.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/demo.gif)

<!-- The database in the screenshot is the sample database in MySQL ported to SQLite, downloaded from https://github.com/fracpete/employees-db-sqlite. -->

## Feature Overview
This extension can be used to 📊 view and edit database contents, ⚙ view and edit table schema, and ▶️ execute SQL queries.

<img src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/three-parts-v2.png" width="650px">

Here are some videos of the main features:

## 📊 Viewing Database Contents

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/view-database-contents.mp4" controls></video>

The key features of the table viewer in this extension are:

- This extension uses **scrolling** for browsing records, which should be more intuitive than pagination.
- **Only the data that is currently visible on the screen is retrieved** from the database, so it loads quickly even on large databases.
- The data is **automatically reloaded** when the table is modified by another process.

It also comes with various auxiliary features such as conditional formatting, 'Group by Value', image BLOB previews, foreign key hover, etc.

## 📊 Editing Database Contents

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/edit-database-contents.mp4" controls></video>

In addition to simple [UPDATE](https://www.sqlite.org/lang_update.html)s and [INSERT](https://www.sqlite.org/lang_insert.html)s shown in the recording above, you can bulk-set a value to a selection, delete multiple rows by dragging over row numbers, set a value to a cell in a foreign key column using a dropdown, edit a table via a view, etc.

## ⚙ Editing Table Schema

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/edit-table-schema.mp4" controls></video>

You can edit table schemas as shown in the video. In addition to [tables](https://www.sqlite.org/lang_createtable.html), you can also edit a [view](https://www.sqlite.org/lang_createview.html)'s name and definition.

## ▶️ Executing SQL Queries
![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/query-editor.gif)

You can run arbitrary queries in the query editor. The editor supports **context-aware auto-completion, syntax highlighting, hover documentation, signature help, and syntax validation**.


# Feature Documentation
The features listed in this section are not in any particular order.
Feel free to explore each one as you like.

Table of Contents
- [Creating a Database](#creating-a-database)
- [Editing Table Schema - Checking Table Schema](#editing-table-schema---checking-table-schema)
- [Editing Table Schema - Changing Column Definition](#editing-table-schema---changing-column-definition)
- [Editing Table Schema - Changing Column Order](#editing-table-schema---changing-column-order)
- [Editing Table Schema - Creating a Table](#editing-table-schema---creating-a-table)
- [Editing Table Schema - Creating an Index](#editing-table-schema---creating-an-index)
- [Editing Table Schema - Dropping a Table](#editing-table-schema---dropping-a-table)
- [Editing Table Schema - Renaming a Table](#editing-table-schema---renaming-a-table)
- [File Associations](#file-associations)
- [Importing and Exporting Data in CSV, JSON, or SQL](#importing-and-exporting-data-in-csv-json-or-sql)
- [In-Memory Databases](#in-memory-databases)
- [Opening the Database in a Command Line Shell](#opening-the-database-in-a-command-line-shell)
- [Query Editor - Overview](#query-editor---overview)
- [Query Editor - Document Formatting](#query-editor---document-formatting)
- [Query Editor - Executing a Part of Common Table Expression (CTE)](#query-editor---executing-a-part-of-common-table-expression-cte)
- [Query Editor - Syntax Validation](#query-editor---syntax-validation)
- [Table View - Auto Reloading](#table-view---auto-reloading)
- [Table View - Conditional Formatting](#table-view---conditional-formatting)
- [Table View - Displaying and Jumping to the Definition of Foreign Keys](#table-view---displaying-and-jumping-to-the-definition-of-foreign-keys)
- [Table View - Drop Multiple Tables](#table-view---drop-multiple-tables)
- [Table View - Editing GENERATED Columns](#table-view---editing-generated-columns)
- [Table View - Entity-Relationship Diagram](#table-view---entity-relationship-diagram)
- [Table View - Filtering and Sorting Data](#table-view---filtering-and-sorting-data)
- [Table View - Finding Foreign Keys Referencing a Value](#table-view---finding-foreign-keys-referencing-a-value)
- [Table View - Git-Diff Support](#table-view---git-diff-support)
- [Table View - Group by Value](#table-view---group-by-value)
- [Table View - Inserting Data from CSV](#table-view---inserting-data-from-csv)
- [Table View - Jumping to a Table or a Row](#table-view---jumping-to-a-table-or-a-row)
- [Table View - Multi-Selection](#table-view---multi-selection)
- [Table View - Pop-Out Editor](#table-view---pop-out-editor)
- [Table View - Resizing Columns](#table-view---resizing-columns)
- [Table View - Resizing Rows](#table-view---resizing-rows)
- [Table View - Selecting a Table](#table-view---selecting-a-table)
- [Table View - Tabs](#table-view---tabs)
- [Using Run-Time Loadable SQLite Extensions](#using-run-time-loadable-sqlite-extensions)
- [Using User Compiled SQLite](#using-user-compiled-sqlite)

## Creating a Database
To create [a database file](https://www.sqlite.org/onefile.html), simply create a file with a supported file extension, such as .db, .sqlite, or .sqlite3. The extension will automatically initialize the file as a database if it is empty and has one of the supported extensions.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/new-database.gif)


## Editing Table Schema - Checking Table Schema
To view the schema of the active table, click on the "Schema" button located at the top of the editor. This will open a panel displaying the table schema, [indexes](https://www.sqlite.org/lang_createindex.html), and [triggers](https://www.sqlite.org/lang_createtrigger.html). This feature supports both [tables](https://www.sqlite.org/lang_createtable.html) and [views](https://www.sqlite.org/lang_createview.html).

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-schema-v2.png)

The "Index" section displays an array of blue and gray boxes for each index. They represent which column the index applies to, with numbers indicating the order. For example, if you have `CREATE TABLE table1(a, b, c); CREATE INDEX index1 ON table1 (c, a)`, then the coloring of the boxes would be `blue, gray, blue`, and the numbers would be `2, -, 1`.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/index-visualization.png)

When you hover your cursor over an index, it highlights the corresponding columns. Conversely, when you hover your cursor over the dotted text in the columns, it highlights the associated indexes in the "Schema" pane.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/index-hover.png)


## Editing Table Schema - Changing Column Definition
You can change the [type affinity](https://www.sqlite.org/datatype3.html#type_affinity) and the [constraints](https://www.sqlite.org/syntax/column-constraint.html) of a column with this feature.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/change-type.png)


## Editing Table Schema - Changing Column Order
You can change the order of table columns by dragging the table header.

We've tested this feature extensively, but we won't take any responsibility for possible data loss. Please ensure you check the generated query and/or create a backup before using this feature, especially if you're working with a critical database.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/reorder-columns.gif)


## Editing Table Schema - Creating a Table
You can access this feature by clicking on the statement at the bottom of the editor, then selecting "CREATE TABLE".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/editors.png)

The tables that can be created by this feature are limited to simpler ones. To create a complex table, such as ones with [GENERATED columns](https://www.sqlite.org/gencol.html) or [COLLATE clauses](https://www.sqlite.org/lang_createtable.html#the_collate_clause), use the query editor.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/create-table.png)


## Editing Table Schema - Creating an Index
You can access this feature by either clicking the SQL statement at the bottom of the editor, right-clicking the table name in the SELECT statement, or clicking "Schema" then "Index > + Add".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/editors.png)

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-selector-contextmenu.png)

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-schema-v2.png)


## Editing Table Schema - Dropping a Table
You can access this feature by either clicking on the SQL statement at the bottom of the editor, or by right-clicking the table name in the SELECT statement, and then selecting "DROP TABLE".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/editors.png)

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-selector-contextmenu.png)


## Editing Table Schema - Renaming a Table
To rename a table, right-click the table name in the SELECT statement, and then select "Rename Table".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/table-selector-contextmenu.png)


## File Associations
This extension recognizes `.db`, `.db3`, `.sdb`, `.s3db`, `.sqlitedb`, `.mddata`, `.sqlite`, `.sqlite3`, `.sl3`, `.vscdb`, and `.sq3` files as database files. To open other files, right-click the file in the explorer and select `Open with…` then `SQLite3 Editor`.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/open_with.gif)


## Importing and Exporting Data in CSV, JSON, or SQL
By clicking the "Other Tools..." button, you can access various features, including CSV, JSON, and SQL imports and exports.
These import and export features rely on a helper program bundled with this extension. You can check the available options by using `<command> import --help` or `<command> export --help`.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/other-tools.png)


## In-Memory Databases
You can connect to an in-memory database using `SQLite3 Editor: Connect to In-Memory Database` in the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette). Alternatively, you can connect by editing the first line in a query editor to `--database: :memory:` (for details, refer to the "Query Editor" section).
This feature should be useful to quickly test SQL statements.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/in-memory.png)


## Opening the Database in a Command Line Shell
This feature opens an integrated terminal in VSCode, initialized with the command `sqlite3 <your-file>`. 
It is available only if you have the `sqlite3` command installed on your system. 
To use this feature, navigate to "Other Tools" then "Open in Command Line Shell".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/open-in-command-line-shell.png)


## Query Editor - Overview
To access the query editor, click the "Query Editor" button.

The line comment at the first line of the query editor indicates the linked database. If it is deleted, the query editor will disconnect from the database.

Any files that start with `-- database: ...` will be recognized as a query editor. This allows you to save a query editor as a file for future use.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/query-editor-file.gif)

There are three ways to execute statements in the query editor:
- To run a single statement, use `Shift+Enter` (or ⇧ return on Mac) or click the "Execute" button above the statement. The result will only be displayed if it is a SELECT statement. To display the result of PRAGMA statements, use the pragma functions (e.g. use `SELECT * FROM pragma_table_list();` instead of `PRAGMA table_list;`).
- To execute the entire file, use the ▷ button located in the top right corner of the editor.
- To execute a part of the file, select the text then click "Execute Selection" in the context menu.

The "Execute" button shown above a transaction (`BEGIN;` ... `END;` block) executes all the statements in the transaction. If the transaction is not successfully executed, the extension will perform a [ROLLBACK](https://www.sqlite.org/lang_transaction.html).

Due to the limitation of the current mechanism to reload the table, there may be a slight delay between the execution of a statement and the updates to the table.


## Query Editor - Document Formatting
You can format queries by selecting "Format Document" in the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) or by pressing Shift+Alt+F (or ⇧ ⌥ F on Mac).

This feature employs [sql-formatter](https://github.com/sql-formatter-org/sql-formatter) to format queries.
You can adjust formatting options with the configurations under `sqlite3-editor.format`, and they are mostly compatible with [Prettier SQL VSCode](https://marketplace.visualstudio.com/items?itemName=inferrinizzard.prettier-sql-vscode).

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/format.gif)


## Query Editor - Executing a Part of Common Table Expression (CTE)
In the query editor, "Select" buttons are displayed for each CTE. This enhances the ease of creating complex queries involving CTEs.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/cte.gif)


## Query Editor - Syntax Validation
The query editor identifies syntax errors in SQL statements by [preparing](https://www.sqlite.org/c3ref/prepare.html) each statement in an isolated database connection and catching compilation errors.
However, due to the nature of this method, certain errors might not be detected, such as those within PRAGMA statements or references to non-existent tables.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/syntax-validator.png)


## Table View - Auto Reloading
When the 'Auto Reload' button is activated, the editor will automatically refresh the table whenever there are updates.

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/auto-reload.mp4" controls></video>


## Table View - Conditional Formatting
Conditional formatting colorizes table cells by their values. You can use this feature by right-clicking a table column then "Colorize (Conditional Formatting)".


## Table View - Displaying and Jumping to the Definition of Foreign Keys
You can view the source record of a cell in a column that is under a [foreign key constraint](https://www.sqlite.org/foreignkeys.html) by hovering the cursor over the cell.
If you want to jump to the source record, use the context menu item.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/hover-fk.gif)

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/goto-fk.gif)


## Table View - Drop Multiple Tables
You can quickly drop multiple tables with the multiselect mode in the table selector. You can enter the multiselect mode by right-clicking on a table name in the dropdown menu or by pressing Alt+Click (or ⌥ click on Mac) on a dropdown item.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/multiselect.png)


## Table View - Editing GENERATED Columns
[GENERATED columns](https://www.sqlite.org/gencol.html) can be edited just like any other columns. Committing a change updates the table schema.

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/edit-generated-always-as.mp4" controls></video>


## Table View - Entity-Relationship Diagram
If the database contains [foreign keys](https://www.sqlite.org/foreignkeys.html) or [views](https://www.sqlite.org/lang_createview.html), the table selector will display the entity-relationship diagram alongside the list of tables. Clicking on an entity opens the corresponding table.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/erd.png)

You can display the columns and values in the first row of a table by right-clicking on the table name or pressing Ctrl+Click (or ⌘ click on Mac).


## Table View - Filtering and Sorting Data
The find widget shown in the image below allows you to quickly filter records by searching for text matches across all columns, just like [the one in VSCode](https://code.visualstudio.com/docs/editor/codebasics#_find-and-replace). For more advanced usage, you can also use the regular expression, whole word, and case-sensitivity switches.
You can access this feature by pressing the "Find" button in the editor or pressing Ctrl+F (or ⌘ F on Mac).

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/find_widget.png)

Column filters allow you to filter records based on a specific value in the chosen column. To use this, right-click on a table column header.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/column-filter.png)

Alternatively, you can also set a filter via the context menu on cells.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/set-filter.png)

To sort records by a specific column, simply click on the column name. You can also sort the table from the context menu on the column name.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/sorting.png)


## Table View - Finding Foreign Keys Referencing a Value
To find the foreign keys referencing a value, select a cell and click `Find All References` in the context menu or press Shift+F12 (or ⇧ F12 on Mac).

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/find-all-references.mp4" controls></video>


## Table View - Git-Diff Support
When you open a database from [the source control view](https://code.visualstudio.com/docs/sourcecontrol/overview), you will see a side-by-side comparison of two versions of the database.

To display the differences between the two versions, click the "Compare with Local File" button. Depending on the size of the database, it may take several seconds or minutes for the differences to appear. If locking the databases is a problem for your use-case, you should avoid using this feature.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/diff.gif)


## Table View - Group by Value
You can group records by a column with this feature. To group a column, right-click on a column header then select "Group by Value". To cancel the grouping, click the icon on the column header.

<video src="https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/group-by.mp4" controls></video>


## Table View - Inserting Data from CSV
You can insert CSV into an existing table by clicking the SQL statement at the bottom of the editor then selecting "Bulk Insert".

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/editors.png)

This feature inserts CSV data into the table. Each CSV column is encoded as TEXT, but if the table column has a data type (column affinity), SQLite will cast it to the appropriate type. For example, if a column is defined as "column1 INTEGER," then the CSV values in that column will be cast as an integer.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/bulk-insert.png)


## Table View - Jumping to a Table or a Row
When the extension's editor is active, you can use the Go to Table/Row command to navigate to a specific table and/or row. The Ctrl+G keybinding (or ⌘ G on Mac) is assigned to this command.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/goto.gif)


## Table View - Multi-Selection
[UPDATE](https://www.sqlite.org/lang_update.html) and [DELETE](https://www.sqlite.org/lang_delete.html) statements support multi-selection. To select multiple cells, you can either drag over the cells, click a cell with the alt key pressed, or press the Shift + Arrow keys while a cell is selected.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/multi-select.gif)

> Dragging on row numbers is not currently supported, and you need to use the alt + click instead.

You can perform actions other than editing data by right-clicking on the selection.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/multi-select-contextmenu.png)


## Table View - Pop-Out Editor
This feature is available when the configuration `sqlite3-editor.ui.experimental.popOutEditor.enabled` is set to `true`. The default setting is `false`.

When enabled, you can open an embedded textarea in a new tab by either:
- Clicking the button displayed at the top-left corner of the currently focused textarea.
- Pressing Alt+P (or ⌥P on Mac).

The Alt+P shortcut selects an editor based on the following rules:
1. If an editor is focused, then it is chosen.
2. If there are editors in the bottom or side pane, then the topmost one among them is chosen.
3. Otherwise, the topmost editor is chosen.

Setting `sqlite3-editor.ui.popOutEditor.enabled` to true also adds the `Ctrl + S` keybinding to the UI for consistency with the pop-out editors. When pressed, it asks if the changes should be committed.


## Table View - Resizing Columns
You can resize columns by dragging the right edge of the column header. Alternatively, to adjust the width to the content, you can use the "Autofit Column Width" button in the context menu.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/autofit.gif)


## Table View - Resizing Rows
You can resize rows by dragging the lower edge of a row's number.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/resize-rows.png)


## Table View - Selecting a Table
You can switch between tables by clicking a table name in either the editor or the explorer.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/switch-table-2.gif)


## Table View - Tabs
Adding `"sqlite3-editor.ui.alwaysDisplayTabs": true` to VSCode's settings enables the table tab feature.
Its behavior resembles that of VSCode's tabs; in [the preview mode](https://code.visualstudio.com/docs/getstarted/userinterface#_preview-mode), the tab closes when you switch to another table, but after double-clicking the preview tab, the tab remains open until you click the close button.
Certain actions, such as selecting "Go to Source Record" on foreign key columns, activate the tab UI regardless of the value of the `sqlite3-editor.ui.alwaysDisplayTabs` setting.

![](https://raw.githubusercontent.com/yy0931/sqlite3-editor/main/tabs.png)


## Using Run-Time Loadable SQLite Extensions
The configuration setting "sqlite3-editor.connection.runtimeLoadableExtensions" allows you to specify [run-time loadable extensions](https://www.sqlite.org/loadext.html) that will be loaded with every SQLite connection opened by this extension.

For example, to load SpatiaLite, follow these instructions:

1. Install SpatiaLite:
   ```shell
   # Ubuntu/Debian
   sudo apt install libsqlite3-mod-spatialite
   
   # macOS
   brew install libspatialite

   # Windows
   Download a binary from https://www.gaia-gis.it/gaia-sins/, extract it, and add the directory containing mod_spatialite.dll to the PATH environment variable. You may need to reopen the VSCode window.
   ```
2. Configure the extension (`F1` or `Ctrl(Cmd) + Shift + P` -> `Preferences: Open User Settings (JSON)`):
   ```json
   "sqlite3-editor.connection.runtimeLoadableExtensions": {
       ".*": ["mod_spatialite"]
   }
   ```

   Run-time loadable extensions can be associated with specific files by matching them with a regex pattern. To match any file, use ".*".


## Using User Compiled SQLite
Since this extension statically links SQLite to a component built with Rust, you need to rebuild the component to use a non-standard version of SQLite.

For example, if you want to add the compilation flag [SQLITE_OMIT_DEPRECATED](https://www.sqlite.org/compile.html#omit_deprecated) to SQLite to exclude deprecated features, follow these instructions:
1. First, you need to install [Rust](https://www.rust-lang.org/tools/install) and [Git](https://git-scm.com/).
2. Then, build the Rust component with the following commands. Note that this project uses the "bundled" [feature](https://doc.rust-lang.org/cargo/reference/features.html) of the [libsqlite3-sys](https://crates.io/crates/libsqlite3-sys) crate, and [libsqlite3-sys](https://crates.io/crates/libsqlite3-sys) uses the "LIBSQLITE3_FLAGS" environment variable when compiling the SQLite source.
   ```shell
   git clone https://github.com/yy0931/sqlite3-editor --single-branch --branch rust-backend
   cd sqlite3-editor
   cargo clean
   LIBSQLITE3_FLAGS='-DSQLITE_OMIT_DEPRECATED' cargo build --release --features sqlite
   ```
3. Finally, specify the absolute path to `./target/release/sqlite3-editor` in the `sqlite3-editor.executablePath` setting of VSCode.

Please note that making changes like this could cause issues with future updates to the extension. Therefore, we recommend turning off automatic updates for this extension.

# Frequently Asked Questions
- Q: How can I input NULL quickly?\
  A: Select a cell, press Shift+Alt+N (or ⇧ ⌥ N on Mac), then press Ctrl+Enter (or ⌘ ↩ on Mac).
- Q: How can I delete all the rows in a table quickly?\
  A: There is no button to do that in the UI. Execute `DELETE FROM <table-name>;` in the query editor.
- Q: The UI is too compact.\
  A: You can increase the value of "Sqlite3-editor › UI: Spacing" ("sqlite3-editor.ui.spacing") in the VSCode settings.
- Q: How can I save a query I wrote in the query editor?\
  A: You can save the editor content as a file with Ctrl+S (or ⌘ S on Mac). You may want to change the file path on the first line of the file to a relative path, such as `-- database: ./database.sqlite`, to ensure it works when the parent folder is renamed or moved. If you frequently use a SELECT statement, also consider creating a [view](https://www.sqlite.org/lang_createview.html).
- Q: Can I open the result of a SELECT statement, which I executed in the query editor, in another editor tab?\
  A: Currently, there is no direct way to do that. However, the query result is shown in the most recently active UI tab. Therefore, you can duplicate the editor tab for the database file using the "Split Editor Right" button at the top right corner, click on the newly opened editor tab's title to make it active, then execute the query to send the result to that new editor tab.
- Q: What is 'rowid = ...' in the tooltip on row numbers? It shows a different number than the row number.\
  A: It is the rowid in [ROWID tables](https://www.sqlite.org/rowidtable.html).

# Configurations
This document does not cover all of the configuration options. Please search "sqlite3-editor" in the VSCode's settings tab for further information.

## sqlite3-editor.connection.setupQueries
This configuration specifies SQL statements that are executed immediately after connecting to a database.

The keys are case-sensitive regular expressions used to match the file URI, and the values are corresponding SQL statements to be executed. In case multiple patterns match the same URI, only the first item will be used.

Commands that are available in the SQLite's CLI, including `.load`, are not supported. To load run-time loadable extensions, use the `sqlite3-editor.connection.runtimeLoadableExtensions` configuration instead.

For example, to execute [`PRAGMA foreign_keys = ON;`](https://www.sqlite.org/pragma.html#pragma_foreign_keys) and [`PRAGMA busy_timeout = 1000;`](https://www.sqlite.org/pragma.html#pragma_busy_timeout) on all SQLite 3 connections, you can specify the following configuration:

```json
"sqlite3-editor.connection.setupQueries": {
    ".*": "PRAGMA foreign_keys = ON; PRAGMA busy_timeout = 1000;"
}
```


## sqlite3-editor.connection.runtimeLoadableExtensions
This configuration loads [run-time loadable extensions](https://www.sqlite.org/loadext.html) immediately after connecting to a database, using the `sqlite3_load_extension` call in the SQLite C interface.

The keys are case-sensitive regular expressions used to match the file URI, and the values are the list of runtime-loadable extensions to be loaded. In case multiple patterns match the same URI, only the first item will be used. The runtime-loadable extensions are loaded before executing the setup queries specified in `sqlite3-editor.connection.setupQueries`.

For example, to load the `crypto` module in sqlean, download and extract a release of [sqlean](https://github.com/nalgeon/sqlean), and specify the extracted path as follows:

```json
"sqlite3-editor.connection.runtimeLoadableExtensions": {
  ".*": ["/home/user/sqlean/crypto.so"]
}
```

## sqlite3-editor.pragma_foreign_key
This configuration controls whether the enforcement of foreign key constraints is enabled. This configuration has the same effect as setting `"sqlite3-editor.connection.setupQueries": { ".*": "PRAGMA foreign_keys = <value>;" }`, except changes are applied to open database connections immediately.

## sqlite3-editor.maxHistoryEntries
By default, this extension stores the last 500 SQL queries executed in the query editor. You can view them using `SQLite3 Editor: Show History` and clear them using `SQLite3 Editor: Clear History` from [the command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette). This setting specifies the number of queries to save. If set to 0, history will not be saved.

## sqlite3-editor.comment.filepath
By default, the "comment" feature, accessible from the schema pane, writes descriptions about database tables to a file with the extension ".docs.md" located next to the database table.

This configuration changes the file path of the comment file.

### Syntax
The value can begin with one of the following prefix variables. If the value lacks these prefix variables, it is interpreted as an absolute path.

- `${fileDirname}`: The parent directory of the database file (e.g., `/foo/bar` for `/foo/bar/db.sqlite`).
- `${fileWorkspaceFolder}`: The currently opened folder.
- `${userHome}`: The user's home directory on the computer.

After the prefix or the first segment (e.g., "C:\\" or "/") of the absolute path, the following variables can be used anywhere and any number of times:

- `${fileBasename}`: The basename of the database file (e.g., `db.sqlite` for `/foo/bar/db.sqlite`).
- `${fileBasenameNoExtension}`: The basename of the database file without its extension (e.g., `db` for `/foo/bar/db.sqlite`).
- `${fileExtname}`: The file extension of the database file (e.g., `.sqlite` for `/foo/bar/db.sqlite`).
- `${fileDirnameBasename}`: The name of the parent directory of the database file (e.g., `bar` for `/foo/bar/db.sqlite`).

The configuration value must resolve to a filename that ends with ".md" after variable replacement. Slash and backslash characters ("/", "\\") will be replaced with appropriate ones for the current platform.

# Supported Environments
Minimum Supported VSCode Version: 1.70.0 (July 2022)

Supported Operating Systems:

| OS | CPU Architecture | Note |
|--|--|--|
| Windows 7 and later | x64 | |
| Windows 7 and later | IA-32 | |
| Windows 8 and later | ARM64 | |
| Linux | x64 | If glibc version 2.17 or higher is available, glibc is used; otherwise, statically linked musl is used.<br/>If musl is used, [SQLite runtime loadable extensions](https://www.sqlite.org/loadext.html) are not supported. |
| Linux | ARM64 | Same as above. |
| Linux | ARMv6, ARMv7 | If glibc version 2.29 or higher is available, glibc is used; otherwise, statically linked musl is used.<br/>If musl is used, [SQLite runtime loadable extensions](https://www.sqlite.org/loadext.html) are not supported.<br/>When using glibc, only ARMv7 hard-float is supported. |
| Mac 10.15 (Catalina, Darwin 19) and later | x64 | |
| Mac 11.0 (Big Sur, Darwin 20) and later | ARM64 | |

# License
## Open Source Licenses
The `SQLite3 Editor: Open Source Licenses` command in the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) displays the licenses of the open-source libraries used by this software.

## Notice
SQLite3 Editor  Copyright (C) 2024  https://github.com/yy0931

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
