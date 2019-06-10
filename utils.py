import logging, sys, argparse


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    DISEASE = get_typed_entity(tag_seq, char_seq, 'DISEASE')
    SYMPTOM = get_typed_entity(tag_seq, char_seq, 'SYMPTOM')
    BODY = get_typed_entity(tag_seq, char_seq, 'BODY')
    return DISEASE, SYMPTOM, BODY


def get_typed_entity(tag_seq, char_seq, entity_type):
    bTag = 'B-' + entity_type
    iTag = 'I-' + entity_type
    length = len(char_seq)
    typed_entity = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == bTag:
            if 'ent' in locals().keys():
                typed_entity.append(ent)
                del ent
            ent = char
            if i+1 == length:
                typed_entity.append(ent)
        if tag == iTag:
            if 'ent' not in locals().keys():
                continue
            ent += char
            if i+1 == length:
                typed_entity.append(ent)
        if tag not in [iTag, bTag]:
            if 'ent' in locals().keys():
                typed_entity.append(ent)
                del ent
            continue
    return typed_entity

def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
