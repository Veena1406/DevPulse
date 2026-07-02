from flask import Blueprint, render_template, request, redirect, session
from models.document import Document

document = Blueprint("document", __name__)


# Show all documents
@document.route("/documents")
def documents():

    if "user" not in session:
        return redirect("/login")

    docs = Document.get_all(session["user"])

    return render_template("documents.html", documents=docs)


# New document page
@document.route("/new")
def new_document():

    if "user" not in session:
        return redirect("/login")

    return render_template("editor.html", document=None)


# Save new document
@document.route("/new", methods=["POST"])
def save_document():

    if "user" not in session:
        return redirect("/login")

    title = request.form["title"]
    content = request.form["content"]

    Document.create(title, content, session["user"])

    return redirect("/documents")


# Edit page
@document.route("/edit/<document_id>")
def edit_document(document_id):

    if "user" not in session:
        return redirect("/login")

    doc = Document.get(document_id)

    return render_template("editor.html", document=doc)


# Update document
@document.route("/edit/<document_id>", methods=["POST"])
def update_document(document_id):

    if "user" not in session:
        return redirect("/login")

    title = request.form["title"]
    content = request.form["content"]

    Document.update(document_id, title, content)

    return redirect("/documents")


# Delete document
@document.route("/delete/<document_id>")
def delete_document(document_id):

    if "user" not in session:
        return redirect("/login")

    Document.delete(document_id)

    return redirect("/documents")


# View document
@document.route("/view/<document_id>")
def view_document(document_id):

    if "user" not in session:
        return redirect("/login")

    doc = Document.get(document_id)

    return render_template("view.html", document=doc)