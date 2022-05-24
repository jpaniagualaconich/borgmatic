from flexmock import flexmock

from borgmatic.hooks import cronhub as module


def test_ping_monitor_rewrites_ping_url_for_start_state():
    hook_config = {'ping_url': 'https://example.com/start/abcdef'}
    flexmock(module.requests).should_receive('get').with_args('https://example.com/start/abcdef')

    module.ping_monitor(
        hook_config,
        'config.yaml',
        module.monitor.State.START,
        monitoring_log_level=1,
        dry_run=False,
    )


def test_ping_monitor_rewrites_ping_url_and_state_for_start_state():
    hook_config = {'ping_url': 'https://example.com/ping/abcdef'}
    flexmock(module.requests).should_receive('get').with_args('https://example.com/start/abcdef')

    module.ping_monitor(
        hook_config,
        'config.yaml',
        module.monitor.State.START,
        monitoring_log_level=1,
        dry_run=False,
    )


def test_ping_monitor_rewrites_ping_url_for_finish_state():
    hook_config = {'ping_url': 'https://example.com/start/abcdef'}
    flexmock(module.requests).should_receive('get').with_args('https://example.com/finish/abcdef')

    module.ping_monitor(
        hook_config,
        'config.yaml',
        module.monitor.State.FINISH,
        monitoring_log_level=1,
        dry_run=False,
    )


def test_ping_monitor_rewrites_ping_url_for_fail_state():
    hook_config = {'ping_url': 'https://example.com/start/abcdef'}
    flexmock(module.requests).should_receive('get').with_args('https://example.com/fail/abcdef')

    module.ping_monitor(
        hook_config, 'config.yaml', module.monitor.State.FAIL, monitoring_log_level=1, dry_run=False
    )


def test_ping_monitor_dry_run_does_not_hit_ping_url():
    hook_config = {'ping_url': 'https://example.com'}
    flexmock(module.requests).should_receive('get').never()

    module.ping_monitor(
        hook_config, 'config.yaml', module.monitor.State.START, monitoring_log_level=1, dry_run=True
    )
