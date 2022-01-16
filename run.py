#!/usr/bin/env python3.10
from contact import Contact


def create_contact(fname, lname, phone, email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname, lname, phone, email)
    return new_contact


def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()


def del_contact(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()


def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)


def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Contact.contact_exist(number)


def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()
