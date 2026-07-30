from dataclasses import dataclass


@dataclass
class MailAddress:
    name: str
    domain: str


@dataclass
class Mail:
    sender: MailAddress
    receiver: MailAddress
    subject: str
    body: str


@dataclass
class MailAccount:
    name: str
    inbox: list[Mail]
    outbox: list[Mail]


@dataclass
class MailServer:
    domain: str
    accounts: list[MailAccount]


def show_mail_address(e_mail_address: MailAddress) -> str:
    """Takes an e-mail address as an arugment and returns a readable string containing all of its attribute."""
    return (e_mail_address.name + "@" + e_mail_address.domain)


def show_mail(e_mail: Mail) -> str:
    """Takes an e-mail as an argument and returns a readable string containing all of its attributes."""
    return ("From: " + show_mail_address(e_mail.sender) + "\n"
            + "To: " + show_mail_address(e_mail.receiver) + "\n"
            + "Subject: " + e_mail.subject + "\n\n"
            + e_mail.body)


def show_mail_account(account: MailAccount) -> str:
    """Takes an e-mail acocunt as an argument and returns a readable string containing all of its attribute."""
    return ("Name " + account.name + "\n"
            + "Inbox: " + str(account.inbox) + "\n"
            + "Outbox: " + str(account.outbox))


def show_mail_server(server: MailServer) -> str:
    """Takes an e-mail server as an argument and returns a readable string containing all of its attribute."""
    return ("Domain: " + server.domain + "\n"
            + "Accounts " + str(server.accounts))


def find_server(domain: str, servers: list[MailServer]) -> MailServer | None:
    """Looks for the given domain in the list of servers. If the server is found,
    it is returned. Otherwise, None is returned."""
    for s in servers:
        if s.domain == domain:
            return (s)
    return None


def find_account(account: str, servers: list[MailServer]) -> MailAccount | None:
    """Looks for the given account in a list of accounts on a server and returns it (if found)"""
    for s in servers:
        for a in s.accounts:
            if a == account:
                return a
    return None


def deliver_mail(e_mail: Mail, servers: list[MailServer]) -> bool:
    """Searches for a recipient in a list of servers and attempts to deliver the mail to their account."""
    for mailserver in servers:
        for account in mailserver.accounts:
            match e_mail.receiver:
                case name:
                    if account.name == name.name:
                        account.inbox += [e_mail]
                        return True
    return False


def deliver_all_mail(servers: list[MailServer]):
    """Attempts to deliver the e-mails in the accounts' outboxes using the deliver_mail function.
    The sender address must match the address and acoount name and the server's domain name.
    Mails that fail to meet these criteria will be deleted. Successfully sent e-mails are
    removed from the outbox."""
    for mailserver in servers:
        for account in mailserver.accounts:
            new_outbox = []
            for e_mail in account.outbox:
                address = show_mail_address(e_mail.sender)
                if account.name in address and mailserver.domain in address:
                    deliver_mail(e_mail, servers)
                    if deliver_mail(e_mail, servers) is False:
                        new_outbox += [e_mail]
            account.outbox = new_outbox