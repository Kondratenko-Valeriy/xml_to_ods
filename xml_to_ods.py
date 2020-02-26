import os
import re

from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from transliterate import translit
from tqdm import tqdm


XML_DIR = 'xml'
ODS_DIR = 'ods'
TRANSLIT_BUFFER = {}


def get_xml_files(path):
    files_list = []
    for (dir_path, _, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith('.xml'):
                file_path = os.path.join(dir_path, filename)
                files_list.append(file_path)
    return files_list


def get_xml_attributes(xml):
    soup = BeautifulSoup(xml, features='html.parser')
    attrs = []
    for tag in soup.find_all():
        for attr_name, attr_value in tag.attrs.items():
            attrs.append([TRANSLIT_BUFFER[attr_name], attr_value])
    return attrs


def translit_re(re_obj):
    original = re_obj.group(0)
    transliterated = translit(re_obj.group(0), 'ru', reversed=True)
    TRANSLIT_BUFFER[(re.sub(r'[</>=]', '', transliterated)).lower()] = (re.sub(r'[</>=]', '', original))
    return transliterated


def transliterate_cyrillic_tags(xml):
    xml = re.sub(r'(</?[а-я]+>?)', translit_re, xml, flags=re.IGNORECASE)
    xml = re.sub(r'([а-я0-9.]+=)', translit_re, xml, flags=re.IGNORECASE)
    return xml


def convert_xml_to_ods(xml_dir=XML_DIR, ods_dir=ODS_DIR):
    xml_files = get_xml_files(xml_dir)
    for xml_file in tqdm(xml_files, total=len(xml_files), desc='XML files processed'):
        with open(xml_file, 'r', encoding='cp1251') as f:
            content = f.read()
            content = transliterate_cyrillic_tags(content)
            xml_attributes = get_xml_attributes(content)
            data = {"XML Data": xml_attributes}
            xml_file_name = os.path.basename(xml_file)
            ods_file_path = os.path.join(ods_dir, f'{xml_file_name}.ods')
            save_data(ods_file_path, data)


if __name__ == '__main__':
    convert_xml_to_ods()
