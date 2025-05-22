"""Modulo init """
from .models import exists, get_all
from .crud import add_contact, get_contact, update_contact, delete_contact
from .menu import show_menu, run

__all__ = ["exists", "get_all", "add_contact", "get_contact", "update_contact", "delete_contact", "show_menu", "run"]