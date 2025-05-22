from gestor_contactos.crud import add_contact, get_contact, update_contact, delete_contact
from gestor_contactos.models import contacts


def test_contacts_initial_state():
    assert {} == contacts

def test_add_contact():
    return_add_contact = add_contact(
        cedula="0999999999",
        nombres="Juan Andrade",
        celular="0999999999"
    )
    return_add_second_contact = add_contact(
        cedula="0999999999",
        nombres="Juan Andrade",
        celular="0999999999"
    )
    assert (True, "¡Agregado con éxito!") == return_add_contact
    assert (False, "Existe un contacto con esa cédula.") == return_add_second_contact

# def test_get_contact():
#     add_contact(
#         cedula="0988888888",
#         nombres="Juan Andrade",
#         celular="0999999999"
#     )
#     assert None == get_contact("")
#     assert (True, "") == get_contact("0988888888")

def test_get_contact():
    return_get_contact = get_contact (
        cedula = "0999999999"
    )
    return_get_second_contact = get_contact (
        cedula = "1205334574"
    )
    assert (True, "Exito: Contacto encontrado") == return_get_contact
    assert (False, "Error: El contacto no existe.") == return_get_second_contact

def test_update_contact():
    return_update_contact = update_contact (
        cedula = "0999999999",
        nombres = "Heymi Liseth",
        celular ="0981990422"
    )
    return_update_second_contact = update_contact (
        cedula = "08888888888",
        nombres = "Liseth",
        celular ="0981990422"
    )
    assert (True, "¡Modificado con éxito!") == return_update_contact
    assert (False, "Error: El contacto no existe.") == return_update_second_contact

def test_delete_contact():
    return_delete_contact = delete_contact (
        cedula = "0222222222"
    )
    return_delete_second_contact = delete_contact (
        cedula = "0999999999"
    )
    assert (False, "Error: No existe el contacto para eliminar.") == return_delete_contact
    assert (True, "¡Eliminado con éxito.!") == return_delete_second_contact



# from gestor_contactos.menu import run

# def test_run():
#     return_run = run(
#         cedula="0999999999",
#         nombres="Juan Andrade",
#         celular="0999999999"
#     )
#     assert "¡Agregado con éxito!" == return_run