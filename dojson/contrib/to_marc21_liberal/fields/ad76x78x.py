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

from ..model import to_marc21_liberal_authority


@to_marc21_liberal_authority.over('762', '^established_heading_linking_entry_medium_of_performance_term$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_established_heading_linking_entry_medium_of_performance_term(self, key, value):
    """Reverse - Established Heading Linking Entry-Medium of Performance Term."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'institution_to_which_field_applies': '5',
        'control_subfield': 'w',
        'field_link_and_sequence_number': '8',
        'linkage': '6',
        'medium_of_performance_term_as_entry_element': 'a',
        'authority_record_control_number_or_standard_number': '0',
        'relationship_information': 'i',
        'source_of_heading_or_term': '2',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'w': value.get('control_subfield'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '6': value.get('linkage'),
        'a': value.get('medium_of_performance_term_as_entry_element'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '2': value.get('source_of_heading_or_term'),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('780', '^subdivision_linking_entry_general_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subdivision_linking_entry_general_subdivision(self, key, value):
    """Reverse - Subdivision Linking Entry-General Subdivision."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_subdivision': 'y',
        'source_of_heading_or_term': '2',
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'geographic_subdivision': 'z',
        'relationship_information': 'i',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('781', '^subdivision_linking_entry_geographic_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subdivision_linking_entry_geographic_subdivision(self, key, value):
    """Reverse - Subdivision Linking Entry-Geographic Subdivision."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_subdivision': 'y',
        'source_of_heading_or_term': '2',
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'geographic_subdivision': 'z',
        'relationship_information': 'i',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('782', '^subdivision_linking_entry_chronological_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subdivision_linking_entry_chronological_subdivision(self, key, value):
    """Reverse - Subdivision Linking Entry-Chronological Subdivision."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_subdivision': 'y',
        'source_of_heading_or_term': '2',
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'geographic_subdivision': 'z',
        'relationship_information': 'i',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('785', '^subdivision_linking_entry_form_subdivision$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_subdivision_linking_entry_form_subdivision(self, key, value):
    """Reverse - Subdivision Linking Entry-Form Subdivision."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'institution_to_which_field_applies': '5',
        'form_subdivision': 'v',
        'linkage': '6',
        'control_subfield': 'w',
        'chronological_subdivision': 'y',
        'source_of_heading_or_term': '2',
        'authority_record_control_number_or_standard_number': '0',
        'general_subdivision': 'x',
        'geographic_subdivision': 'z',
        'relationship_information': 'i',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        'v': utils.reverse_force_list(
            value.get('form_subdivision')
        ),
        '6': value.get('linkage'),
        'w': value.get('control_subfield'),
        'y': utils.reverse_force_list(
            value.get('chronological_subdivision')
        ),
        '2': value.get('source_of_heading_or_term'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number_or_standard_number')
        ),
        'x': utils.reverse_force_list(
            value.get('general_subdivision')
        ),
        'z': utils.reverse_force_list(
            value.get('geographic_subdivision')
        ),
        'i': utils.reverse_force_list(
            value.get('relationship_information')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict


@to_marc21_liberal_authority.over('788', '^complex_linking_entry_data$')
@utils.filter_values
def reverse_complex_linking_entry_data(self, key, value):
    """Reverse - Complex Linking Entry Data."""
    indicator_map2 = {"Canadian Subject Headings": "5", "LC subject headings for children\u0027s literature": "1", "Library of Congress Subject Headings": "0", "Medical Subject Headings": "2", "National Agricultural Library subject authority file": "3", "R\\xc3\\xa9pertoire de vedettes-mati\\xc3\\xa8re": "6", "Source not specified": "4", "Source specified in subfield $2": "7"}
    field_map = {
        'institution_to_which_field_applies': '5',
        'source_of_heading_or_term': '2',
        'linkage': '6',
        'heading_referred_to': 'a',
        'explanatory_text': 'i',
        'field_link_and_sequence_number': '8',
        'relationship_code': '4',
    }

    order = utils.map_order(field_map, value, liberal=True, indicators=['None', 'thesaurus'])

    record_dict = {
        '__order__': tuple(order) if len(order) else None,
        '5': utils.reverse_force_list(
            value.get('institution_to_which_field_applies')
        ),
        '2': value.get('source_of_heading_or_term'),
        '6': value.get('linkage'),
        'a': utils.reverse_force_list(
            value.get('heading_referred_to')
        ),
        'i': utils.reverse_force_list(
            value.get('explanatory_text')
        ),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '4': utils.reverse_force_list(
            value.get('relationship_code')
        ),
        '$ind1': value.get('$ind1', '_'),
        '$ind2': '7' if 'thesaurus' in value and
        not indicator_map2.get(value.get('thesaurus')) and
        value.get('thesaurus') == value.get('source_of_heading_or_term') and
        field_map.get('thesaurus') in order
        else indicator_map2.get(value.get('thesaurus'), value.get('thesaurus', '_')),
    }

    for subfield_key in value.keys():
        if subfield_key not in field_map.keys() and len(subfield_key) == 1:
            record_dict[subfield_key] = value[subfield_key]

    return record_dict
