def use(d):
    #d at the moment is a dictionary with three elements
    assert d['message']=='OK'
    a = d['data']
    assert len(a) == 1
    b=a[int(0)]
    c = b['securityData']
    e = c['fieldData']
    #c is now a list of all the things.
    return e


