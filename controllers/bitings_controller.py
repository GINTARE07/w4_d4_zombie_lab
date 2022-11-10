from flask import Blueprint, Flask, redirect, render_template, request
from repositories import human_repository, zombie_repository, biting_repository
from models.biting import Biting

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings=bitings)


# NEW
@bitings_blueprint.route("/bitings/new")
def new_bitings():
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/new.html", humans=humans, zombies=zombies)

# CREATE
@bitings_blueprint.route("/bitings", methods=["POST"])
def create_bitings():

    human = human_repository.select(request.form["human_id"])
    zombie = zombie_repository.select(request.form["zombie_id"])
    new_biting = Biting(human, zombie)
    biting_repository.save(new_biting)
    return redirect("/bitings")


# EDIT
@bitings_blueprint.route("/bitings/<id>/edit")
def edit_bitings(id):
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    biting = biting_repository.select(id)
    return render_template('bitings/edit.html', biting=biting, humans=humans, zombies=zombies)


# UPDATE
@bitings_blueprint.route("/bitings/<id>", methods=["POST"])
def update_bitings(id):
    human = human_repository.select(request.form["human_id"])
    zombie = zombie_repository.select(request.form["zombie_id"])
    bitings = Biting(human, zombie, id)
    biting_repository.update(bitings)
    return redirect("/bitings")


# DELETE
@bitings_blueprint.route("/bitings/<id>/delete", methods=["POST"])
def delete_bitings(id):
    biting_repository.delete(id)
    return redirect("/bitings")
