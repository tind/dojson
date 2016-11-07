# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21_liberal


@to_marc21_liberal.over('760', '^main_series_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_main_series_entry(self, key, value):
    """Reverse - Main Series Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Main series": "_", "No display constant generated": "8"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'qualifying_information': 'c',
        'record_control_number': 'w',
        'uniform_title': 's',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'international_standard_serial_number': 'x',
        'physical_description': 'h',
        'related_parts': 'g',
        'linkage': '6',
        'note': 'n',
        'coden_designation': 'y',
        'edition': 'b',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'c': value.get('qualifying_information'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('uniform_title'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        'b': value.get('edition'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('762', '^subseries_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subseries_entry(self, key, value):
    """Reverse - Subseries Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Has subseries": "_", "No display constant generated": "8"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'qualifying_information': 'c',
        'record_control_number': 'w',
        'uniform_title': 's',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'international_standard_serial_number': 'x',
        'physical_description': 'h',
        'related_parts': 'g',
        'linkage': '6',
        'note': 'n',
        'coden_designation': 'y',
        'edition': 'b',
        'material_specific_details': 'm',
        'other_item_identifier': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'c': value.get('qualifying_information'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('uniform_title'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        'b': value.get('edition'),
        'm': value.get('material_specific_details'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('765', '^original_language_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_original_language_entry(self, key, value):
    """Reverse - Original Language Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Translation of": "_"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('767', '^translation_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_entry(self, key, value):
    """Reverse - Translation Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Translated as": "_"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('770', '^supplement_special_issue_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_special_issue_entry(self, key, value):
    """Reverse - Supplement/Special Issue Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Has supplement": "_", "No display constant generated": "8"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('772', '^supplement_parent_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_supplement_parent_entry(self, key, value):
    """Reverse - Supplement Parent Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Parent": "0", "Supplement to": "_"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('773', '^host_item_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_host_item_entry(self, key, value):
    """Reverse - Host Item Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"In": "_", "No display constant generated": "8"}
    field_map = {
        'main_entry_heading': 'a',
        'abbreviated_title': 'p',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'enumeration_and_first_page': 'q',
        'report_number': 'r',
        'record_control_number': 'w',
        'place_publisher_and_date_of_publication': 'd',
        'materials_specified': '3',
        'international_standard_serial_number': 'x',
        'international_standard_book_number': 'z',
        'linkage': '6',
        'edition': 'b',
        'other_item_identifier': 'o',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'note': 'n',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'p': value.get('abbreviated_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'q': value.get('enumeration_and_first_page'),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        '3': value.get('materials_specified'),
        'x': value.get('international_standard_serial_number'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '6': value.get('linkage'),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('774', '^constituent_unit_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_constituent_unit_entry(self, key, value):
    """Reverse - Constituent Unit Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Constituent unit": "_", "No display constant generated": "8"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('775', '^other_edition_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_edition_entry(self, key, value):
    """Reverse - Other Edition Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Other edition available": "_"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'record_control_number': 'w',
        'place_publisher_and_date_of_publication': 'd',
        'international_standard_serial_number': 'x',
        'international_standard_book_number': 'z',
        'linkage': '6',
        'edition': 'b',
        'country_code': 'f',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'standard_technical_report_number': 'u',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'language_code': 'e',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'note': 'n',
        'material_specific_details': 'm',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'x': value.get('international_standard_serial_number'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '6': value.get('linkage'),
        'b': value.get('edition'),
        'f': value.get('country_code'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'u': value.get('standard_technical_report_number'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'e': value.get('language_code'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'm': value.get('material_specific_details'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('776', '^additional_physical_form_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_additional_physical_form_entry(self, key, value):
    """Reverse - Additional Physical Form Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Available in another form": "_", "No display constant generated": "8"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('777', '^issued_with_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_issued_with_entry(self, key, value):
    """Reverse - Issued With Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Issued with": "_", "No display constant generated": "8"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'qualifying_information': 'c',
        'record_control_number': 'w',
        'uniform_title': 's',
        'place_publisher_and_date_of_publication': 'd',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'international_standard_serial_number': 'x',
        'physical_description': 'h',
        'related_parts': 'g',
        'linkage': '6',
        'note': 'n',
        'coden_designation': 'y',
        'edition': 'b',
        'material_specific_details': 'm',
        'series_data_for_related_item': 'k',
        'other_item_identifier': 'o',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'c': value.get('qualifying_information'),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        's': value.get('uniform_title'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        '6': value.get('linkage'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'y': value.get('coden_designation'),
        'b': value.get('edition'),
        'm': value.get('material_specific_details'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('780', '^preceding_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_preceding_entry(self, key, value):
    """Reverse - Preceding Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Absorbed": "5", "Absorbed in part": "6", "Continues": "0", "Continues in part": "1", "Formed by the union of ... and ...": "4", "Separated from": "7", "Supersedes": "2", "Supersedes in part": "3"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'type_of_relationship'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_relationship'), value.get('type_of_relationship', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('785', '^succeeding_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_succeeding_entry(self, key, value):
    """Reverse - Succeeding Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Absorbed by": "4", "Absorbed in part by": "5", "Changed back to": "8", "Continued by": "0", "Continued in part by": "1", "Merged with ... to form ...": "7", "Split into ... and ...": "6", "Superseded by": "2", "Superseded in part by": "3"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'type_of_relationship'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('type_of_relationship'), value.get('type_of_relationship', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('786', '^data_source_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_data_source_entry(self, key, value):
    """Reverse - Data Source Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"Data source": "_", "No display constant generated": "8"}
    field_map = {
        'main_entry_heading': 'a',
        'abbreviated_title': 'p',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'record_control_number': 'w',
        'place_publisher_and_date_of_publication': 'd',
        'international_standard_serial_number': 'x',
        'international_standard_book_number': 'z',
        'linkage': '6',
        'edition': 'b',
        'other_item_identifier': 'o',
        'period_of_content': 'j',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'note': 'n',
        'source_contribution': 'v',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        'p': value.get('abbreviated_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'd': value.get('place_publisher_and_date_of_publication'),
        'x': value.get('international_standard_serial_number'),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        '6': value.get('linkage'),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'j': value.get('period_of_content'),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'v': value.get('source_contribution'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal.over('787', '^other_relationship_entry$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_other_relationship_entry(self, key, value):
    """Reverse - Other Relationship Entry."""
    indicator_map1 = {"Display note": "0", "Do not display note": "1"}
    indicator_map2 = {"No display constant generated": "8", "Related item": "_"}
    field_map = {
        'main_entry_heading': 'a',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
        'report_number': 'r',
        'linkage': '6',
        'place_publisher_and_date_of_publication': 'd',
        'note': 'n',
        'international_standard_book_number': 'z',
        'record_control_number': 'w',
        'edition': 'b',
        'other_item_identifier': 'o',
        'qualifying_information': 'c',
        'material_specific_details': 'm',
        'uniform_title': 's',
        'relationship_information': 'i',
        'control_subfield': '7',
        'title': 't',
        'physical_description': 'h',
        'related_parts': 'g',
        'coden_designation': 'y',
        'international_standard_serial_number': 'x',
        'standard_technical_report_number': 'u',
        'series_data_for_related_item': 'k',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['note_controller', 'display_constant_controller'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('main_entry_heading'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        'r': utils.reverse_force_list(
            value.get('report_number')
        ),
        '6': value.get('linkage'),
        'd': value.get('place_publisher_and_date_of_publication'),
        'n': utils.reverse_force_list(
            value.get('note')
        ),
        'z': utils.reverse_force_list(
            value.get('international_standard_book_number')
        ),
        'w': utils.reverse_force_list(
            value.get('record_control_number')
        ),
        'b': value.get('edition'),
        'o': utils.reverse_force_list(
            value.get('other_item_identifier')
        ),
        'c': value.get('qualifying_information'),
        'm': value.get('material_specific_details'),
        's': value.get('uniform_title'),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '7': value.get('control_subfield'),
        't': value.get('title'),
        'h': value.get('physical_description'),
        'g': utils.reverse_force_list(
            value.get('related_parts')
        ),
        'y': value.get('coden_designation'),
        'x': value.get('international_standard_serial_number'),
        'u': value.get('standard_technical_report_number'),
        'k': utils.reverse_force_list(
            value.get('series_data_for_related_item')
        ),
        '$ind1': indicator_map1.get(value.get('note_controller'), value.get('note_controller', '_')),
        '$ind2': indicator_map2.get(value.get('display_constant_controller'), value.get('display_constant_controller', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
