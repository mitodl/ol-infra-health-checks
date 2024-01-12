def test_xpro_lms(host):
    lms = host.docker("lms")
    assert lms.is_running
    assert lms.is_enabled
