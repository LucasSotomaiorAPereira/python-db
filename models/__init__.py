import models
import models.address
import models.algorithm
import models.base
import models.bet
import models.board
import models.branch
import models.client
import models.employee
import models.game
import models.machine
import models.order
import models.charge
import models.person
import models.payment
import models.product
import models.service
import models.board_employee
import models.board_game
import models.machine_algorithm
import models.order_charge
import models.order_product
import models.order_service
import models.person_address
from services.db import engine


def create_db():
    models.base.Base.metadata.create_all(bind=engine)
