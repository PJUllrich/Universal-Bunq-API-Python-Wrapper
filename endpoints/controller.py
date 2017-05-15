from endpoints.annual_overview import AnnualOverview
from endpoints.attachment_public import AttachmentPublic
from endpoints.attachment_tab import AttachmentTab
from endpoints.avatar import Avatar
from endpoints.customer_statement import CustomerStatement
from endpoints.draft_share_invite_bank import DraftShareInviteBank
from endpoints.share_invite_bank_inquiry import ShareInviteBankInquiry
from endpoints.share_invite_bank_response import ShareInviteBankResponse
from endpoints.card import Card
from endpoints.cash_register import CashRegister
from endpoints.certificate_pinned import CertificatePinned
from endpoints.chat_conversation import ChatConversation
from endpoints.draft_payment import DraftPayment
from endpoints.invoice import Invoice
from endpoints.master_card_action import MasterCardAction
from endpoints.monetary_account import MonetaryAccount
from endpoints.payment import Payment
from endpoints.request_inquiry import RequestInquiry
from endpoints.schedule import Schedule
from endpoints.scheduled_payment import ScheduledPayment
from endpoints.tab import Tab
from endpoints.user import User


class Controller:

    def __init__(self, api_client):
        self.api_client = api_client
        self.user = User(api_client)
        self.monetary_account = MonetaryAccount(api_client)
        self.card = Card(api_client)
        self.payment = Payment(api_client)
        self.request_inquiry = RequestInquiry(api_client)
        self.draft_payment = DraftPayment(api_client)
        self.schedule = Schedule(api_client)
        self.scheduled_payment = ScheduledPayment(api_client)
        self.cash_register = CashRegister(api_client)
        self.master_card_action = MasterCardAction(api_client)
        self.chat_conversation = ChatConversation(api_client)
        self.certificate_pinned = CertificatePinned(api_client)
        self.invoice = Invoice(api_client)
        self.annual_overview = AnnualOverview(api_client)
        self.attachment_public = AttachmentPublic(api_client)
        self.attachment_tab = AttachmentTab(api_client)
        self.avatar = Avatar(api_client)
        self.customer_statement = CustomerStatement(api_client)
        self.draft_invite = DraftShareInviteBank(api_client)
        self.share_inquiry = ShareInviteBankInquiry(api_client)
        self.share_response = ShareInviteBankResponse(api_client)
        self.tab = Tab(api_client)
