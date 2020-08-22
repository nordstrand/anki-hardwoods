import os
import genanki
from pathlib import Path

DATA_PATH="./woods"
ANKI_PACKAGE_PATH="hardwoods.apkg"

model = genanki.Model(
  1252513531,
  'Hardwood Simple Model',
  fields=[
    {'name': 'Art'},
    {'name': 'Latin'},
    {'name': 'FloraIllustration'},
  ],
  templates=[
    {
      'name': 'Art-kort',
      'qfmt': 'Art <br>{{FloraIllustration}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Art}} ({{Latin}})',
    },
    {
      'name': 'Latin-kort',
      'qfmt': 'Latin <br>{{FloraIllustration}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Latin}} ({{Art}})',
    },
  ])

clozeModel = genanki.Model(
  998863322,
  'Hardwood Cloze Model',
  fields=[
    {'name': 'Art'},
    {'name': 'Latin'},
    {'name': 'FloraIllustration'},
    {'name': 'keyInfo'},
  ],
  templates=[
    {
        'name': 'Nyckelinformationkort',
        'qfmt': '{{FloraIllustration}}<br/>{{cloze:keyInfo}}',
        'afmt': '{{cloze:keyInfo}}',
    },
  ],
  model_type=genanki.Model.CLOZE)



def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def getNoteFields(wood):
    with open('woods/' + wood + '/fields.txt') as f:
        art=f.readline().rstrip()
        latin=f.readline().rstrip()
        keyInfo=f.readline().rstrip()
        floraIllustration='<img src="' + wood + '-flora.jpg" />'
        print(f" {art},{latin},{floraIllustration},{keyInfo}")
        return (art, latin, floraIllustration, keyInfo)

deck = genanki.Deck(
  2063130111,
  'Swedish hard woods')

for wood in get_immediate_subdirectories(DATA_PATH):
    woodFields = list(getNoteFields(wood))
    deck.add_note(genanki.Note(model=model, fields=woodFields[:-1]))
    deck.add_note(genanki.Note(model=clozeModel, fields=woodFields))
    
package = genanki.Package(deck)
package.media_files = list(map(str, Path(DATA_PATH).rglob('**/*.jpg')))
print(package.media_files)
package.write_to_file(ANKI_PACKAGE_PATH)

print(f"Anki output file {ANKI_PACKAGE_PATH} written.")


with open("release_notes.md", "w") as text_file:
  newLine="\n"
  print(f"""### Hard woods in this release:
{ newLine.join([f" * {wood.title()}" for wood in sorted(get_immediate_subdirectories(DATA_PATH))]) }
  """, file=text_file)