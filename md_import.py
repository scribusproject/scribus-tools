run_script = True

import scribus
from tempfile import NamedTemporaryFile

try:
    import markdown
except:
    scribus.messageBox('python-markdown not installed',
    'You need to install python-markdown for this script to work', scribus.ICON_WARNING)
    run_script = False

run_script &= bool(scribus.getSelectedObject(0))  # We must have at least one selected object

if run_script and scribus.getSelectedObject(1):
    result = scribus.messageBox('', 'More than one item selected, load all?',
                                button1=scribus.BUTTON_CANCEL, button2=scribus.BUTTON_YES)

    if result == scribus.BUTTON_CANCEL:
        run_script = False

def main():
    md_name = scribus.fileDialog("Select a file", 'Markdown (*.md)')
    if not md_name:
        return

    f = NamedTemporaryFile(suffix='.html')
    markdown.markdownFromFile(md_name, f)
    f.flush()
    
    html_name = f.name

    i = 0
    while True:
        ob_name = scribus.getSelectedObject(i)

        if not ob_name:
            break

        if scribus.getObjectType(ob_name) == 'TextFrame':
            scribus.insertHtmlText(html_name, ob_name)

        i += 1

if run_script:
    main()
