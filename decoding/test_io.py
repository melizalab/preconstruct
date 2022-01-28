from decoding.io import NeurobankSource

def test_neurobank():
    stimuli = ['ztqee46x',
            '00oagdl5',
            'g29wxi4q',
            'mrel2o09',
            'vekibwgj',
            'l1a3ltpy',
            'igmi8fxa',
            'c95zqjxq',
            'w08e1crn',
            'jkexyrd5',
            'p1mrfhop',
            ]
    responses = ['P120_1_1_c92']
    source = NeurobankSource('https://gracula.psyc.virginia.edu/neurobank/', responses, stimuli)
    assert len(source.get_responses()) == 1
    assert len(source.get_stimuli()) == len(stimuli)
