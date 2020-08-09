import os
import genanki
from pathlib import Path

DATA_PATH="./woods"
ANKI_PACKAGE_PATH="hardwoods.apkg"

model = genanki.Model(
  1252503538,
  'Simple Model',
  fields=[
    {'name': 'Art'},
    {'name': 'Latin'},
    {'name': 'FloraIllustration'},
  ],
  templates=[
    {
      'name': 'Art',
      'qfmt': 'Art <br>{{FloraIllustration}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Art}}',
    },
    {
      'name': 'Latin',
      'qfmt': 'Latin <br>{{FloraIllustration}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Latin}}',
    },
  ])


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def getNoteFields(wood):
    with open('woods/' + wood + '/fields.txt') as f:
        art=f.readline().rstrip()
        latin=f.readline().rstrip()
        floraIllustration='<img src="' + wood + '-flora.jpg">'
        print(f" {art},{latin},{floraIllustration}")
        return (art, latin, floraIllustration)

deck = genanki.Deck(
  2022400110,
  'Swedish hard woods')

for wood in get_immediate_subdirectories(DATA_PATH):
    deck.add_note(genanki.Note(model=model, fields=list(getNoteFields(wood))))
    
package = genanki.Package(deck)
package.media_files = list(map(str, Path(DATA_PATH).rglob('**/*.jpg')))
print(package.media_files)
package.write_to_file(ANKI_PACKAGE_PATH)

print(f"Anki output file {ANKI_PACKAGE_PATH} written.")