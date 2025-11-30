#!/usr/bin/env python3
"""
Qt6 Hello World Application for Windows
A demonstration application with menu, toolbar, treeview, and about dialog.
"""

import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QTreeWidget, QTreeWidgetItem, QToolBar, QPushButton,
    QMessageBox, QStatusBar, QHeaderView
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt  # noqa: F401 - may be used for flags


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt6 Hello World")
        self.setMinimumSize(600, 400)
        self.resize(800, 600)

        self._create_menu_bar()
        self._create_toolbar()
        self._create_central_widget()
        self._create_status_bar()

    def _create_menu_bar(self):
        """Create the file menu with about and exit options."""
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("&File")

        # Exit action
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit the application")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Help menu
        help_menu = menu_bar.addMenu("&Help")

        # About action
        about_action = QAction("&About", self)
        about_action.setStatusTip("About this application")
        about_action.triggered.connect(self._show_about_dialog)
        help_menu.addAction(about_action)

        # About Qt action
        about_qt_action = QAction("About &Qt", self)
        about_qt_action.setStatusTip("About Qt framework")
        about_qt_action.triggered.connect(QApplication.aboutQt)
        help_menu.addAction(about_qt_action)

    def _create_toolbar(self):
        """Create the toolbar with a button."""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Add items button
        add_button = QPushButton("Add Random Items")
        add_button.setStatusTip("Add random items to the tree")
        add_button.clicked.connect(self._add_random_items)
        toolbar.addWidget(add_button)

        # Clear button
        clear_button = QPushButton("Clear Tree")
        clear_button.setStatusTip("Clear all items from the tree")
        clear_button.clicked.connect(self._clear_tree)
        toolbar.addWidget(clear_button)

        # Refresh button
        refresh_action = QAction("Refresh", self)
        refresh_action.setStatusTip("Regenerate all items")
        refresh_action.triggered.connect(self._regenerate_tree)
        toolbar.addAction(refresh_action)

    def _create_central_widget(self):
        """Create the central widget with a treeview."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create tree widget
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Name", "Type", "Value"])
        self.tree.setAlternatingRowColors(True)
        self.tree.setSortingEnabled(True)

        # Configure header
        header = self.tree.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        layout.addWidget(self.tree)

        # Populate with initial random items
        self._populate_tree()

    def _create_status_bar(self):
        """Create the status bar."""
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")

    def _populate_tree(self):
        """Populate the tree with random items."""
        categories = [
            ("Fruits", ["Apple", "Banana", "Cherry", "Date", "Elderberry"]),
            ("Animals", ["Aardvark", "Bear", "Cat", "Dog", "Eagle"]),
            ("Colors", ["Red", "Green", "Blue", "Yellow", "Purple"]),
            ("Countries", ["USA", "Canada", "Japan", "Germany", "Brazil"]),
        ]

        for category_name, items in categories:
            category_item = QTreeWidgetItem([category_name, "Category", ""])
            self.tree.addTopLevelItem(category_item)

            # Add random subset of items
            selected_items = random.sample(items, random.randint(2, len(items)))
            for item_name in selected_items:
                value = random.randint(1, 100)
                child_item = QTreeWidgetItem([item_name, "Item", str(value)])
                category_item.addChild(child_item)

            category_item.setExpanded(True)

        self.statusBar().showMessage(f"Loaded {self.tree.topLevelItemCount()} categories")

    def _add_random_items(self):
        """Add random items to the tree."""
        random_names = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"]
        random_types = ["TypeA", "TypeB", "TypeC"]

        # Add to a random existing category or create new
        if self.tree.topLevelItemCount() > 0 and random.random() > 0.3:
            parent_index = random.randint(0, self.tree.topLevelItemCount() - 1)
            parent = self.tree.topLevelItem(parent_index)
        else:
            parent = QTreeWidgetItem([f"NewCategory_{random.randint(1, 99)}", "Category", ""])
            self.tree.addTopLevelItem(parent)
            parent.setExpanded(True)

        # Add 1-3 random children
        for _ in range(random.randint(1, 3)):
            name = random.choice(random_names) + str(random.randint(1, 99))
            item_type = random.choice(random_types)
            value = random.randint(1, 1000)
            child = QTreeWidgetItem([name, item_type, str(value)])
            parent.addChild(child)

        self.statusBar().showMessage("Added random items")

    def _clear_tree(self):
        """Clear all items from the tree."""
        self.tree.clear()
        self.statusBar().showMessage("Tree cleared")

    def _regenerate_tree(self):
        """Regenerate all tree items."""
        self.tree.clear()
        self._populate_tree()
        self.statusBar().showMessage("Tree regenerated")

    def _show_about_dialog(self):
        """Show the about dialog."""
        QMessageBox.about(
            self,
            "About Qt6 Hello World",
            "<h2>Qt6 Hello World</h2>"
            "<p>Version 1.0.0</p>"
            "<p>A demonstration application built with Python and PySide6 (Qt 6).</p>"
            "<p>Features:</p>"
            "<ul>"
            "<li>File menu with exit option</li>"
            "<li>Toolbar with action buttons</li>"
            "<li>TreeView with random data</li>"
            "<li>About dialog</li>"
            "</ul>"
            "<p>Built to test Qt6 packaging for Windows.</p>"
        )


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    app.setApplicationName("Qt6 Hello World")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Demo")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
