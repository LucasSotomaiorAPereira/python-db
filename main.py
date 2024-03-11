from models import *
from models.enum import client_type, emp_function, order_status
from services.db import session
from datetime import date, datetime
from sqlalchemy import select


def insert():
    with session:
        session.add_all([
            models.address.Address(
                street="Rua 1",
                district="Bairro 1",
                city="Cidade 1",
                state="Estado 1",
                country="Pais 1"),
            models.address.Address(
                street="Rua 2",
                district="Bairro 2",
                city="Cidade 2",
                state="Estado 2",
                country="Pais 2"),
            models.address.Address(
                street="Rua 3",
                district="Bairro 3",
                city="Cidade 3",
                state="Estado 3",
                country="Pais 3"),
            models.address.Address(
                street="Rua 4",
                district="Bairro 4",
                city="Cidade 4",
                state="Estado 4",
                country="Pais 4"),
            models.address.Address(
                street="Rua 5",
                district="Bairro 5",
                city="Cidade 5",
                state="Estado 5",
                country="Pais 5"),
            models.address.Address(
                street="Rua 6",
                district="Bairro 6",
                city="Cidade 6",
                state="Estado 6",
                country="Pais 6"),
        ])
        session.commit()

        session.add_all([
            models.branch.Branch(
                name="Filial 1",
                cnpj="1111111",
                address_id=1),
            models.branch.Branch(
                name="Filial 2",
                cnpj="2222222",
                address_id=2),
            models.branch.Branch(
                name="Filial 3",
                cnpj="3333333",
                address_id=3),
            models.branch.Branch(
                name="Filial 4",
                cnpj="4444444",
                address_id=4),
            models.branch.Branch(
                name="Filial 5",
                cnpj="5555555",
                address_id=5),
            models.branch.Branch(
                name="Filial 6",
                cnpj="6666666",
                address_id=6),
        ])
        session.commit()

        session.add_all([
            models.person.Person(
                name="Nome 1",
                lastname="Sobrenome 1",
                cpf="111111111",
                rg="111111111",
                email="email1@email.com",
                birthdate=date.today(),
                phone="111111111",
                branch_id=1),
            models.person.Person(
                name="Nome 2",
                lastname="Sobrenome 2",
                cpf="222222222",
                rg="222222222",
                email="email2@email.com",
                birthdate=date.today(),
                phone="222222222",
                branch_id=1),
            models.person.Person(
                name="Nome 3",
                lastname="Sobrenome 3",
                cpf="333333333",
                rg="333333333",
                email="email3@email.com",
                birthdate=date.today(),
                phone="333333333",
                branch_id=2),
            models.person.Person(
                name="Nome 4",
                lastname="Sobrenome 4",
                cpf="444444444",
                rg="444444444",
                email="email4@email.com",
                birthdate=date.today(),
                phone="444444444",
                branch_id=2),
            models.person.Person(
                name="Nome 5",
                lastname="Sobrenome 5",
                cpf="555555555",
                rg="555555555",
                email="email5@email.com",
                birthdate=date.today(),
                phone="555555555",
                branch_id=3),
            models.person.Person(
                name="Nome 6",
                lastname="Sobrenome 6",
                cpf="666666666",
                rg="666666666",
                email="email6@email.com",
                birthdate=date.today(),
                phone="666666666",
                branch_id=3),
            models.person.Person(
                name="Nome 7",
                lastname="Sobrenome 7",
                cpf="777777777",
                rg="777777777",
                email="email7@email.com",
                birthdate=date.today(),
                phone="777777777",
                branch_id=4),
            models.person.Person(
                name="Nome 8",
                lastname="Sobrenome 8",
                cpf="888888888",
                rg="888888888",
                email="email8@email.com",
                birthdate=date.today(),
                phone="888888888",
                branch_id=5),
        ])
        session.commit()

        session.add_all([
            models.employee.Employee(
                person_id=1,
                function=emp_function.EmployeeFunction.MANAGER),
            models.employee.Employee(
                person_id=2,
                function=emp_function.EmployeeFunction.WAITER),
            models.employee.Employee(
                person_id=3,
                function=emp_function.EmployeeFunction.SELLER),
            models.employee.Employee(
                person_id=4,
                function=emp_function.EmployeeFunction.WAITER),
            models.employee.Employee(
                person_id=7,
                function=emp_function.EmployeeFunction.HUMAN_RESOURCES),
            models.employee.Employee(
                person_id=8,
                function=emp_function.EmployeeFunction.HUMAN_RESOURCES),
            models.client.Client(
                person_id=1,
                type=client_type.ClientType.STANDARD),
            models.client.Client(
                person_id=2,
                type=client_type.ClientType.STANDARD),
            models.client.Client(
                person_id=3,
                type=client_type.ClientType.VIP),
            models.client.Client(
                person_id=4,
                type=client_type.ClientType.VIP_PLUS_PLUS),
            models.client.Client(
                person_id=5,
                type=client_type.ClientType.VIP_PLUS),
            models.client.Client(
                person_id=6,
                type=client_type.ClientType.SUBSCRIBER),
        ])
        session.commit()

        session.add_all([
            models.person_address.PersonAddress(
                person_id=1,
                address_id=1),
            models.person_address.PersonAddress(
                person_id=2,
                address_id=2),
            models.person_address.PersonAddress(
                person_id=3,
                address_id=3),
            models.person_address.PersonAddress(
                person_id=4,
                address_id=4),
            models.person_address.PersonAddress(
                person_id=5,
                address_id=5),
            models.person_address.PersonAddress(
                person_id=6,
                address_id=6),
        ])
        session.commit()

        session.add_all([
            models.machine.Machine(
                name="Machine 1",
                description="Win machine 1",
                created_at=datetime.now(),
                activated=True,
                branch_id=1),
            models.machine.Machine(
                name="Machine 2",
                description="Win machine 2",
                created_at=datetime.now(),
                activated=False,
                branch_id=2),
            models.machine.Machine(
                name="Machine 3",
                description="Win machine 3",
                created_at=datetime.now(),
                activated=True,
                branch_id=1),
            models.machine.Machine(
                name="Machine 4",
                description="Win machine 4",
                created_at=datetime.now(),
                activated=True,
                branch_id=3),
            models.machine.Machine(
                name="Machine 5",
                description="Win machine 5",
                created_at=datetime.now(),
                activated=False,
                branch_id=5),
            models.machine.Machine(
                name="Machine 6",
                description="Win machine 6",
                created_at=datetime.now(),
                activated=True,
                branch_id=4),
        ])
        session.commit()

        session.add_all([
            models.algorithm.Algorithm(
                description="Win algorithm 1",
                code_url="https://code_url_1.com",
                created_at=datetime.now()),
            models.algorithm.Algorithm(
                description="Win algorithm 2",
                code_url="https://code_url_2.com",
                created_at=datetime.now()),
            models.algorithm.Algorithm(
                description="Win algorithm 3",
                code_url="https://code_url_3.com",
                created_at=datetime.now()),
            models.algorithm.Algorithm(
                description="Win algorithm 4",
                code_url="https://code_url_4.com",
                created_at=datetime.now()),
            models.algorithm.Algorithm(
                description="Win algorithm 5",
                code_url="https://code_url_5.com",
                created_at=datetime.now()),
            models.algorithm.Algorithm(
                description="Win algorithm 6",
                code_url="https://code_url_6.com",
                created_at=datetime.now()),
        ])
        session.commit()

        session.add_all([
            models.machine_algorithm.MachineAlgorithm(
                machine_id=1,
                algorithm_id=1),
            models.machine_algorithm.MachineAlgorithm(
                machine_id=2,
                algorithm_id=2),
            models.machine_algorithm.MachineAlgorithm(
                machine_id=3,
                algorithm_id=2),
            models.machine_algorithm.MachineAlgorithm(
                machine_id=4,
                algorithm_id=4),
            models.machine_algorithm.MachineAlgorithm(
                machine_id=5,
                algorithm_id=1),
            models.machine_algorithm.MachineAlgorithm(
                machine_id=2,
                algorithm_id=3),
        ])
        session.commit()

        session.add_all([
            models.board.Board(
                number=12,
                available=True,
                branch_id=1),
            models.board.Board(
                number=2,
                available=True,
                branch_id=2),
            models.board.Board(
                number=31,
                available=True,
                branch_id=1),
            models.board.Board(
                number=4,
                available=True,
                branch_id=4),
            models.board.Board(
                number=10,
                available=True,
                branch_id=3),
            models.board.Board(
                number=15,
                available=True,
                branch_id=6),
        ])
        session.commit()

        session.add_all([
            models.game.Game(
                name="Game 1",
                description="Description 1",
                max_players=5,
                min_players=1,
                max_bet=600.0,
                min_bet=100.0),
            models.game.Game(
                name="Game 2",
                description="Description 2",
                max_players=10,
                min_players=3,
                max_bet=750.0,
                min_bet=250.0),
            models.game.Game(
                name="Game 3",
                description="Description 3",
                max_players=7,
                min_players=2,
                max_bet=200.0,
                min_bet=50.0),
            models.game.Game(
                name="Game 4",
                description="Description 4",
                max_players=20,
                min_players=5,
                max_bet=3000.0,
                min_bet=500.0),
            models.game.Game(
                name="Game 5",
                description="Description 5",
                max_players=2,
                min_players=2,
                max_bet=200.0,
                min_bet=200.0),
            models.game.Game(
                name="Game 6",
                description="Description 6",
                max_players=3,
                min_players=3,
                max_bet=300.0,
                min_bet=100.0),
        ])
        session.commit()

        session.add_all([
            models.board_employee.BoardEmployee(
                board_id=1,
                employee_id=1),
            models.board_employee.BoardEmployee(
                board_id=2,
                employee_id=3),
            models.board_employee.BoardEmployee(
                board_id=3,
                employee_id=4),
            models.board_employee.BoardEmployee(
                board_id=4,
                employee_id=1),
            models.board_employee.BoardEmployee(
                board_id=5,
                employee_id=3),
            models.board_employee.BoardEmployee(
                board_id=6,
                employee_id=4),
        ])
        session.commit()

        session.add_all([
            models.order.Order(
                created_at=datetime.now(),
                status=order_status.OrderStatus.CREATED,
                person_id=1),
            models.order.Order(
                created_at=datetime.now(),
                status=order_status.OrderStatus.PAID,
                person_id=2),
            models.order.Order(
                created_at=datetime.now(),
                status=order_status.OrderStatus.CREATED,
                person_id=3),
            models.order.Order(
                created_at=datetime.now(),
                status=order_status.OrderStatus.PAID,
                person_id=2),
            models.order.Order(
                created_at=datetime.now(),
                status=order_status.OrderStatus.DELIVERED,
                person_id=4),
            models.order.Order(
                created_at=datetime.now(),
                status=order_status.OrderStatus.CREATED,
                person_id=1),
        ])
        session.commit()

        session.add_all([
            models.charge.Charge(
                name="Credit 1",
                description="Credit Card 1",
                created_at=datetime.now()),
            models.charge.Charge(
                name="Credit 2",
                description="Credit Card 2",
                created_at=datetime.now()),
            models.charge.Charge(
                name="Debit 1",
                description="Debit Card 1",
                created_at=datetime.now()),
            models.charge.Charge(
                name="Debit 2",
                description="Debit Card 2",
                created_at=datetime.now()),
            models.charge.Charge(
                name="Money",
                description="Money",
                created_at=datetime.now()),
            models.charge.Charge(
                name="Pix",
                description="Pix",
                created_at=datetime.now()),
        ])
        session.commit()

        session.add_all([
            models.payment.Payment(
                value=1900.0,
                date=datetime.now(),
                employee_id=1),
            models.payment.Payment(
                value=799.99,
                date=datetime.now(),
                employee_id=1),
            models.payment.Payment(
                value=300,
                date=datetime.now(),
                employee_id=7),
            models.payment.Payment(
                value=600,
                date=datetime.now(),
                employee_id=7),
            models.payment.Payment(
                value=120,
                date=datetime.now(),
                employee_id=3),
            models.payment.Payment(
                value=1300,
                date=datetime.now(),
                employee_id=1),
        ])
        session.commit()

        session.add_all([
            models.order_charge.OrderCharge(
                order_id=2,
                charge_id=1),
            models.order_charge.OrderCharge(
                order_id=4,
                charge_id=1),
            models.order_charge.OrderCharge(
                order_id=2,
                charge_id=3),
            models.order_charge.OrderCharge(
                order_id=2,
                charge_id=4),
            models.order_charge.OrderCharge(
                order_id=2,
                charge_id=5),
            models.order_charge.OrderCharge(
                order_id=2,
                charge_id=6),
        ])
        session.commit()

        session.add_all([
            models.product.Product(
                name="Produto 1",
                description="Descrição 1",
                price=50.0,
                created_at=datetime.now(),
                stock=5),
            models.product.Product(
                name="Produto 2",
                description="Descrição 2",
                price=99.9,
                created_at=datetime.now(),
                stock=10),
            models.product.Product(
                name="Produto 3",
                description="Descrição 3",
                price=19.9,
                created_at=datetime.now(),
                stock=30),
            models.product.Product(
                name="Produto 4",
                description="Descrição 4",
                price=25.0,
                created_at=datetime.now(),
                stock=5),
            models.product.Product(
                name="Produto 5",
                description="Descrição 5",
                price=15.0,
                created_at=datetime.now(),
                stock=20),
            models.product.Product(
                name="Produto 6",
                description="Descrição 6",
                price=80.0,
                created_at=datetime.now(),
                stock=50),
        ])
        session.commit()

        session.add_all([
            models.service.Service(
                name="Serviço 1",
                description="Descrição 1",
                price=29.9,
                created_at=datetime.now()),
            models.service.Service(
                name="Serviço 2",
                description="Descrição 2",
                price=39.9,
                created_at=datetime.now()),
            models.service.Service(
                name="Serviço 3",
                description="Descrição 3",
                price=19.9,
                created_at=datetime.now()),
            models.service.Service(
                name="Serviço 4",
                description="Descrição 4",
                price=9.9,
                created_at=datetime.now()),
            models.service.Service(
                name="Serviço 5",
                description="Descrição 5",
                price=59.9,
                created_at=datetime.now()),
            models.service.Service(
                name="Serviço 6",
                description="Descrição 6",
                price=99.9,
                created_at=datetime.now()),
        ])
        session.commit()

        session.add_all([
            models.order_product.OrderProduct(
                order_id=1,
                product_id=1),
            models.order_product.OrderProduct(
                order_id=2,
                product_id=2),
            models.order_product.OrderProduct(
                order_id=3,
                product_id=3),
            models.order_product.OrderProduct(
                order_id=4,
                product_id=4),
            models.order_product.OrderProduct(
                order_id=5,
                product_id=5),
            models.order_product.OrderProduct(
                order_id=6,
                product_id=6),
        ])
        session.commit()

        session.add_all([
            models.order_service.OrderService(
                order_id=1,
                service_id=1),
            models.order_service.OrderService(
                order_id=2,
                service_id=2),
            models.order_service.OrderService(
                order_id=3,
                service_id=3),
            models.order_service.OrderService(
                order_id=4,
                service_id=4),
            models.order_service.OrderService(
                order_id=5,
                service_id=5),
            models.order_service.OrderService(
                order_id=6,
                service_id=6),
        ])
        session.commit()

        session.add_all([
            models.bet.Bet(
                value=150.0,
                created_at=datetime.now(),
                win=True,
                machine_id=1,
                person_id=1),
            models.bet.Bet(
                value=300.0,
                created_at=datetime.now(),
                win=False,
                game_id=2,
                person_id=2),
            models.bet.Bet(
                value=100.0,
                created_at=datetime.now(),
                win=False,
                game_id=3,
                person_id=3),
            models.bet.Bet(
                value=650.0,
                created_at=datetime.now(),
                win=True,
                machine_id=4,
                person_id=4),
            models.bet.Bet(
                value=200.0,
                created_at=datetime.now(),
                win=False,
                game_id=5,
                person_id=5),
            models.bet.Bet(
                value=150.0,
                created_at=datetime.now(),
                win=False,
                game_id=6,
                person_id=6),
        ])
        session.commit()


def update():
    statement = select(models.person.Person).where(
        models.person.Person.name.in_(["Nome 1", "Nome 2"]))

    for i, person in enumerate(session.scalars(statement)):
        person.name = "Novo Nome " + str(i + 1)
    session.commit()

    statement = select(models.machine.Machine).where(
        models.machine.Machine.activated == False).where(
        models.machine.Machine.branch_id == 2)

    for i, machine in enumerate(session.scalars(statement)):
        machine.description = "Máquina Desativada"
    session.commit()

    statement = select(models.employee.Employee).where(
        models.employee.Employee.function == emp_function.EmployeeFunction.MANAGER)

    for i, employee in enumerate(session.scalars(statement)):
        employee.function = emp_function.EmployeeFunction.SUB_MANAGER
    session.commit()

    statement = select(models.order.Order).where(
        models.order.Order.status == order_status.OrderStatus.DELIVERED)

    for i, order in enumerate(session.scalars(statement)):
        order.status = order_status.OrderStatus.PAID
    session.commit()

    statement = select(models.address.Address).where(
        models.address.Address.country.in_(["Pais 3", "Pais 4"]))

    for i, address in enumerate(session.scalars(statement)):
        address.city = "São Paulo"
    session.commit()


def delete():
    person_address = session.get(models.person_address.PersonAddress, (3, 3))
    session.delete(person_address)
    session.commit()

    bet = session.get(models.bet.Bet, 3)
    session.delete(bet)
    session.commit()

    employee = session.get(models.employee.Employee, 8)
    session.delete(employee)
    session.commit()

    order = session.get(models.order.Order, 3)
    session.delete(order)
    session.commit()

    person = session.get(models.person.Person, 8)
    session.delete(person)
    session.commit()


if __name__ == "__main__":
    create_db()
    insert()
    update()
    delete()

    machine = models.machine.Machine()
    # print(machine.getActive(id=3))
    # result = machine.getMostUsedMachines()
    # for i, m in enumerate(result):
    #     print(f"Position {i + 1}: Count {m[0]} Machine Id {m[1]}")
    # print(machine.getAllMachinesBets())

    order = models.order.Order()
    # print(order.getStatus(id=4))

    client = models.client.Client()
    # print(client.getType(id=2))
    # print(client.getNumberOfClients())
    # print(client.getAllClientsBets())

    employee = models.employee.Employee()
    # print(employee.getFunction(id=1))
    # print(employee.getNumberOfEmployees())
    # print(employee.getNumberOfEmployeePayments(1))
    # print(employee.getWaitersData())

    board = models.board.Board()
    # print(board.getAvailable(id=1))

    bet = models.bet.Bet()
    # print(bet.getBetValue(id=1))

    person = models.person.Person()
    # print(person.getBets(id=1))
    # result = person.getThreeMostBetPeople()
    # for i, p in enumerate(result):
    #     print(f"Position {i + 1}: Sum {p[0]} Person Id {p[1]}")
    # print(person.getPersonBetsValue(id=1))
    # print(person.getPersonWinRate(id=1))
    # print(person.getNumberOfPeopleInAddress(1))
    # print(person.getNumberOfPersonOrders(1))

    game = models.game.Game()
    # result = game.getMostUsedGames()
    # for i, g in enumerate(result):
    #     print(f"Position {i + 1}: Count {g[0]} Game Id {g[1]}")

    product = models.product.Product()
    # print(product.getStock(id=1))
    # print(product.getPrice(id=1))
    # result = product.getMostBuyedProducts()
    # for i, p in enumerate(result):
    #     print(f"Position {i + 1}: Count {p[0]}, Product Id {p[1]}")

    payment = models.payment.Payment()
    # result = payment.getEmployeePayment(id=1)
    # print(result)

    charge = models.charge.Charge()
    # print(charge.getCreationDate(id=2))
    # result = charge.getMostUsedCharges()
    # for i, c in enumerate(result):
    #     print(f"Position {i + 1}: Count {c[0]} Charge Id {c[1]}")
