from django.core.management.base import BaseCommand

from search.more_like_text_helper import more_like_text


class Command(BaseCommand):
    def handle(self, *args, **options):
        res = more_like_text("""

            S T A T U T O R Y I N S T R U M E N T S
            2018 No. 489
            LAND CHARGES, ENGLAND
            The Local Land Charges Fees (England) Rules 2018
            Made - - - - 16th April 2018
            Laid before Parliament 18th April 2018
            Coming into force - - 14th May 2018
            The Lord Chancellor in exercise of the powers conferred by section 14(1)(h) of the Local Land
            Charges Act 1975(a) and with the concurrence of the Treasury makes the following Rules:
            Citation, commencement, application and interpretation
            1.—(1) These Rules may be cited as the Local Land Charges Fees (England) Rules 2018 and
            shall come into force on 14th May 2018(b).
            (2) These Rules apply in relation to England only.
            (3) In these Rules “the principal Rules” means the Local Land Charges Rules 2018(c).
            (4) Expressions used in these Rules have the meaning which they bear in the principal Rules.
            Fees
            2. The fees for the services specified in the Schedule shall be those set out in that Schedule.
            Method of payment
            3.—(1) The fee shall be payable on delivery of the application or requisition, or lodging of the
            definitive certificate, as appropriate.
            (2) Except where the registrar otherwise permits and, subject to paragraphs (3) and (4), the fee
            shall be paid by credit or debit card.
            (3) Where there is an agreement between the applicant or person requesting the service and the
            registrar, a fee may be paid by direct debit to such bank account of Her Majesty’s Land Registry
            as the registrar may from time to time direct.
            (4) Where an application or requisition is made, or a definitive certificate is lodged, other than
            by using an electronic means of communication, the fee may be paid by cheque or postal order
            crossed and made payable to Her Majesty’s Land Registry.

            (a) 1975 c. 76; section 14(1) was amended by paragraph 13 of Schedule 5 to the Infrastructure Act 2015 (c. 7).
            (b) Under paragraph 40(3) and (4) of Schedule 5 to the Infrastructure Act 2015, these Rules have effect in relation to the area of
            a local authority only on and after the date specified in a notice under paragraph 40(1) of that Schedule.
            (c) S.I. 2018/273.
            2
            Signed by the authority of the Lord Chancellor
            David Gauke
            Secretary of State for Justice
            16th April 2018 Ministry of Justice
            We consent
            Rebecca Harris
            Craig Whittaker
            16th April 2018 Two of the Lords Commissioners of Her Majesty’s Treasury
            3
             SCHEDULE Rule 2
            FEES
            Service Fee

            (1) Registration of a light obstruction notice £18
            (2) Variation of the registration of a light obstruction notice under rule 7(1) of the
            principal Rules
            £18
            (3) Cancellation of the registration of a light obstruction notice under rule 7(1) of the
            principal Rules
            £18
            (4) Variation of the registration of light obstruction notice under rule 7(6) of the
            principal Rules (definitive certificate lodged)
            £18
            (5) Official search of the register (including issue of an official certificate of search)
            under section 9(1) of the Local Land Charges Act 1975
            £15
             Provided that no fee is payable for an official search if the requisition is delivered
            within six months of the delivery by the same person of an earlier requisition for an
            official search which was in respect of the same land and for which the prescribed
            fee was paid.
            4
            £4.25
            UK201804171006 04/2018 19585
            http://www.legislation.gov.uk/id/uksi/2018/489
            EXPLANATORY NOTE
            (This note is not part of the Rules)
            These Rules prescribe the fees payable to the Chief Land Registrar for various services relating to
            local land charges affecting land in England and provided under the Local Land Charges Act 1975
            (c. 76) and the Local Land Charges Rules 2018 (S.I. 2018/273). They replace the fees specified by
            individual local authorities under section 13A of the Local Land Charges Act 1975 for similar
            services relating to local land charges affecting land in their respective administrative areas: this
            section is repealed by the Infrastructure Act 2015 (c. 7) with effect in a local authority area on the
            same day as these Rules have effect in that area.
            The services for which fees are payable are set out in the Schedule. Paragraphs (1) to (4) are
            services in connection with light obstruction notices, which are a particular type of local land
            charge. Under paragraph (5), a fee is payable for an official search of the register, unless an
            application for such a search is received within 6 months of an earlier such application, delivered
            by the same person and in relation to the same land, and being an official search for which a fee
            was paid.
            Rule 3 prescribes when the fees for these services are payable, and how the fees are to be paid.
            A full impact assessment of the effect that the amendments to the Local Land Charges Act 1975
            and this instrument will have on the costs of business, the voluntary sector and the public sector is
            available from the Policy and Stakeholder Team, Trafalgar House, 1 Bedford Park, Croydon, CR0
            2AQ and is published with the Explanatory Memorandum alongside these Rules on
            www.legislation.gov.uk.


            © Crown copyright 2018
            Printed and published in the UK by The Stationery Office Limited under the authority and superintendence of Jeff James,
            Controller of Her Majesty’s Stationery Office and Queen’s Printer of Acts of Parliament.




        """)

        res = more_like_text('LAND CHARGES')
        for hit in res['hits']['hits']:
            print(hit.keys())
            print(hit['highlight'])
            # print(hit['model'].title)
