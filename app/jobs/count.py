from app import app, Printer, Count, db
import app.crawler as crawler
from datetime import datetime

def count():
    with app.app_context():
        printers = Printer.query.filter_by(deleted=False).all()
        for printer in printers:
            fn = getattr(crawler, printer.crawler)
            print "Counting -{}- at -{}- using -{}-".format(
                printer.pat, printer.ip, printer.crawler)
            count = fn(printer.ip)
            if count:
                print "----"
                print "Success!"
                count = int(filter(lambda x: x.isdigit(), count))
                print count
                printer.count = count
                printer.last_count == datetime.now()
                db.session.add(Count(printer.id, count))
                db.session.commit()
            else:
                print "----"
                print "Failed."
            print "Done."
