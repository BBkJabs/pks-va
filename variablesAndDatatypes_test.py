import variablesAndDatatypes;
import io;

def test_hello(capsys):
    variablesAndDatatypes.main()
    captured = capsys.readouterr()
    expected_output = "Die Variable 'ganzzahl' ist vom Datentyp '<class 'int'>' und hat gespeichert: 42\nDie Variable 'kommazahl' ist vom Datentyp '<class 'float'>' und hat gespeichert: 3.14\nDie Variable 'istPythonDoof' ist vom Datentyp '<class 'bool'>' und hat gespeichert: False\nDie Variable 'text' ist vom Datentyp '<class 'str'>' und hat gespeichert: Ich mag Python"
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()

    assert  output == expected_output
