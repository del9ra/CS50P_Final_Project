from project import tickets_csv, accommodation_csv, attractions_csv


def test_tickets():
    assert tickets_csv('italy_tickets.csv', '1') == 890
    assert tickets_csv('turkey_tickets.csv', '2') == 1481
    assert tickets_csv('thailand_tickets.csv', '3') == 4151


def test_accommodation():
    assert accommodation_csv('italy_accommodation.csv', '3') == 826
    assert accommodation_csv('thailand_accommodation.csv', '2') == 196
    assert accommodation_csv('turkey_accommodation.csv', '1') == 98


def test_attractions():
    assert attractions_csv('thailand_free.csv', '10') == 0
    assert attractions_csv('turkey_free.csv', '5') == 0
    assert attractions_csv('italy_free.csv', '8') == 0
    assert attractions_csv('thailand_paid.csv', '9') == 37.29
    assert attractions_csv('italy_paid.csv', '7') == 11.70
