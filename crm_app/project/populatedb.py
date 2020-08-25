from . import constants
from . import models
from . import db
 
if __name__ == "__main__":
    for name, val in constants.Project: #'SKILLZ', 'skillz'
        obj = models.Project(
            name=name
        )
        db.session.add(obj)
        db.session.commit()

    for name, val in constants.Client: 
        obj = models.Client(
            name=name
        )
        db.session.add(obj)
        db.session.commit()

    for name, val in constants.Problem: 
        obj = models.Client(
            name=name
        )
        db.session.add(obj)
        db.session.commit()

    for name, val in constants.Status: 
        obj = models.Client(
            name=name
        )
        db.session.add(obj)
        db.session.commit()

    for name, val in constants.Service: 
        obj = models.Client(
            name=name
        )
        db.session.add(obj)
        db.session.commit()