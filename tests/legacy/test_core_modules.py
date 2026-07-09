"""
Tests for the generated legacy core modules added in this PR:
legacy/core/core_module_001.py .. legacy/core/core_module_012.py

Every one of these modules follows the exact same generated template as the
legacy/config modules (only numeric ids/prefixes differ: "cor"/"COR" instead
of "con"/"CON", and "core" instead of "config"). The tests below are
parametrized across all of them to get full coverage without duplicating
near-identical test code.

The template contains a few genuine (not simulated) bugs that define its
actual runtime behavior, and this suite locks that behavior in:

* ``proc_cor_*`` functions build a value using an undefined name ``fi``
  inside a ``for``/``for`` loop wrapped in ``try/except Exception``. Since
  ``fi`` is never defined anywhere in the module, every single iteration
  raises ``NameError``, which is swallowed and recorded in the returned
  ``"e"`` list. The functions never raise, but they also never produce any
  usable results (``"r"`` stays empty).
* ``LegCOR*`` worker classes reference an undefined name ``ci`` inside their
  background-thread loop (same style of bug), which causes the thread to
  self-terminate quickly after accumulating more than 10 errors. Their
  ``process()`` method references ``self.__l``, a private attribute that is
  never assigned (only ``self.__lk`` is), so calling ``process()`` once the
  worker has been started raises ``AttributeError``.
"""
import importlib
import time

import pytest

CORE_MODULE_IDS = [f"{i:03d}" for i in range(1, 13)]  # 001 .. 012
CLASS_SUFFIXES = ["000", "001", "002", "003"]


def load_module(idx):
    return importlib.import_module(f"legacy.core.core_module_{idx}")


@pytest.fixture(params=CORE_MODULE_IDS, ids=CORE_MODULE_IDS)
def mod(request):
    module = load_module(request.param)
    return module, request.param


class TestModuleLevelConstants:
    def test_c_t_f_triples_follow_generated_pattern(self, mod):
        module, idx = mod
        num = int(idx)
        for k in range(15):
            c = getattr(module, f"C{num}_{k}")
            t = getattr(module, f"T{num}_{k}")
            f = getattr(module, f"F{num}_{k}")
            assert c == 42 + 7 * k
            assert t == f"t{k}_{num}"
            assert f is (k % 2 == 0)

    def test_module_metadata_dict(self, mod):
        module, idx = mod
        num = int(idx)
        meta = getattr(module, f"M{idx}")
        assert meta["id"] == num
        assert meta["d"] == "core"
        assert meta["n"] == f"core_module_{idx}"
        assert isinstance(meta["v"], str) and meta["v"]

    def test_global_state_containers_present(self, mod):
        module, _ = mod
        assert isinstance(module._g_state, dict)
        assert isinstance(module._g_counter, list)
        assert module._g_counter == [0]


class TestProcFunctions:
    @pytest.mark.parametrize("fn_idx", range(15))
    def test_proc_always_returns_internal_error_result(self, mod, fn_idx):
        module, idx = mod
        num = int(idx)
        fn = getattr(module, f"proc_cor_{idx}_{fn_idx:04d}")
        result = fn()
        assert result["ok"] is False
        assert result["r"] == []
        assert result["c"] == 0
        assert result["m"] == num
        # 20 * 20 loop iterations, every single one hits the undefined `fi`
        assert len(result["e"]) == 400
        assert all("fi" in msg for msg in result["e"])

    def test_proc_ignores_its_input_arguments(self, mod):
        module, idx = mod
        fn = getattr(module, f"proc_cor_{idx}_0000")
        default_result = fn()
        custom_result = fn(d={"x": 1}, c={"custom": True}, extra_kw="ignored")
        assert default_result == custom_result

    def test_proc_returns_new_containers_each_call(self, mod):
        module, idx = mod
        fn = getattr(module, f"proc_cor_{idx}_0000")
        first = fn()
        second = fn()
        assert first["r"] is not second["r"]
        assert first["e"] is not second["e"]


class TestHelperFunctions:
    @pytest.mark.parametrize("empty_value", [None, [], {}, "", 0])
    def test_hlp_returns_empty_marker_for_falsy_input(self, mod, empty_value):
        module, idx = mod
        fn = getattr(module, f"hlp_proc_cor_{idx}_0000")
        assert fn(empty_value) == {"s": "empty"}

    def test_hlp_wraps_scalar_input_in_a_list(self, mod):
        module, idx = mod
        fn = getattr(module, f"hlp_proc_cor_{idx}_0000")
        result = fn(42)
        assert result == {"d": ["42"], "vc": 1, "t": 1}

    def test_hlp_counts_non_empty_string_representations(self, mod):
        module, idx = mod
        fn = getattr(module, f"hlp_proc_cor_{idx}_0007")
        result = fn(["a", "", "b", 0])
        assert result["d"] == ["a", "", "b", "0"]
        assert result["t"] == 4
        # "" stringifies to an empty (falsy) string, everything else is truthy
        assert result["vc"] == 3

    @pytest.mark.parametrize("fn_idx", range(15))
    def test_all_hlp_indices_exist_and_are_callable(self, mod, fn_idx):
        module, idx = mod
        fn = getattr(module, f"hlp_proc_cor_{idx}_{fn_idx:04d}")
        assert callable(fn)
        assert fn(None) == {"s": "empty"}


class TestValidationFunctions:
    @pytest.mark.parametrize("bad_input", [None, [], "x", 123, (1, 2)])
    def test_rejects_non_dict_input(self, mod, bad_input):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0000")
        assert fn(bad_input) == {"ok": False, "e": ["need dict"]}

    def test_accepts_dict_when_no_schema_given(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0000")
        result = fn({"a": 1, "b": 2})
        assert result == {"ok": True, "e": [], "t": 2}

    def test_missing_required_field_reported_when_strict(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0001")
        schema = {"p": {"name": {"t": "str"}}}
        result = fn({}, s=schema, st=True)
        assert result["ok"] is False
        assert result["e"] == ["missing name"]
        assert result["t"] == 0

    def test_missing_required_field_ignored_when_not_strict(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0001")
        schema = {"p": {"name": {"t": "str"}}}
        result = fn({}, s=schema, st=False)
        assert result == {"ok": True, "e": [], "t": 0}

    def test_type_mismatch_str(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0002")
        schema = {"p": {"name": {"t": "str"}}}
        result = fn({"name": 123}, s=schema)
        assert result["ok"] is False
        assert "name not str" in result["e"]

    def test_type_mismatch_num(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0002")
        schema = {"p": {"age": {"t": "num"}}}
        result = fn({"age": "old"}, s=schema)
        assert result["ok"] is False
        assert "age not num" in result["e"]

    def test_type_mismatch_arr(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0002")
        schema = {"p": {"tags": {"t": "arr"}}}
        result = fn({"tags": "not-a-list"}, s=schema)
        assert result["ok"] is False
        assert "tags not arr" in result["e"]

    def test_valid_types_pass_for_all_fields(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0003")
        schema = {
            "p": {
                "name": {"t": "str"},
                "age": {"t": "num"},
                "tags": {"t": "arr"},
            }
        }
        result = fn({"name": "bob", "age": 5, "tags": [1, 2]}, s=schema)
        assert result == {"ok": True, "e": [], "t": 3}

    def test_arr_accepts_tuple_as_well_as_list(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0004")
        schema = {"p": {"tags": {"t": "arr"}}}
        result = fn({"tags": (1, 2)}, s=schema)
        assert result == {"ok": True, "e": [], "t": 1}

    def test_unknown_type_key_is_not_validated(self, mod):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_0005")
        schema = {"p": {"anything": {"t": "any"}}}
        result = fn({"anything": object()}, s=schema)
        assert result == {"ok": True, "e": [], "t": 1}

    @pytest.mark.parametrize("fn_idx", range(6))
    def test_all_val_indices_share_the_same_non_dict_behavior(self, mod, fn_idx):
        module, idx = mod
        fn = getattr(module, f"val_cor_{idx}_{fn_idx:04d}")
        assert fn("not-a-dict") == {"ok": False, "e": ["need dict"]}


class TestLegacyWorkerClasses:
    @pytest.mark.parametrize("suffix", CLASS_SUFFIXES)
    def test_default_naming_uses_class_name_and_increments_counter(self, mod, suffix):
        module, idx = mod
        cls = getattr(module, f"LegCOR{idx}{suffix}")
        cls._c = 0  # reset the shared class-level counter for a clean assertion
        first = cls()
        second = cls()
        assert first.n == f"LegCOR{idx}{suffix}_1"
        assert second.n == f"LegCOR{idx}{suffix}_2"
        assert first.s == "init"
        assert first.st == {}
        assert first.ca == {}

    @pytest.mark.parametrize("suffix", CLASS_SUFFIXES)
    def test_custom_name_and_cfg_kwargs_are_merged(self, mod, suffix):
        module, idx = mod
        cls = getattr(module, f"LegCOR{idx}{suffix}")
        obj = cls(nm="custom-name", cfg={"a": 1}, extra="value")
        assert obj.n == "custom-name"
        assert obj.cfg == {"a": 1, "extra": "value"}

    @pytest.mark.parametrize("suffix", CLASS_SUFFIXES)
    def test_start_and_stop_update_status_flag(self, mod, suffix):
        module, idx = mod
        cls = getattr(module, f"LegCOR{idx}{suffix}")
        obj = cls()
        assert obj.start() is obj
        assert obj.s == "running"
        assert obj.stop() is obj
        assert obj.s == "stopped"

    @pytest.mark.parametrize("suffix", CLASS_SUFFIXES)
    def test_background_loop_never_populates_state_due_to_undefined_name(self, mod, suffix):
        module, idx = mod
        cls = getattr(module, f"LegCOR{idx}{suffix}")
        obj = cls()
        obj.start()
        try:
            # the worker loop references an undefined name ("ci") on every
            # attempted assignment, so `st` can never actually be populated
            time.sleep(0.1)
            assert obj.st == {}
        finally:
            obj.stop()

    @pytest.mark.parametrize("suffix", CLASS_SUFFIXES)
    def test_process_before_start_reports_not_running(self, mod, suffix):
        module, idx = mod
        cls = getattr(module, f"LegCOR{idx}{suffix}")
        obj = cls()
        assert obj.process([1, 2, 3]) == {"err": "not running"}

    @pytest.mark.parametrize("suffix", CLASS_SUFFIXES)
    def test_process_after_start_raises_attributeerror(self, mod, suffix):
        module, idx = mod
        cls = getattr(module, f"LegCOR{idx}{suffix}")
        obj = cls()
        obj.start()
        try:
            # process() enters `with self.__l:` but only `self.__lk` was ever
            # assigned in __init__, so this always blows up
            with pytest.raises(AttributeError):
                obj.process([1, 2, 3])
        finally:
            obj.stop()

    @pytest.mark.parametrize("suffix", CLASS_SUFFIXES)
    def test_transform_doubles_numeric_dict_values_only(self, mod, suffix):
        module, idx = mod
        cls = getattr(module, f"LegCOR{idx}{suffix}")
        obj = cls()
        assert obj._t({"a": 2, "b": 3.5, "c": "x"}) == {"a": 4, "b": 7.0, "c": "x"}

    @pytest.mark.parametrize("suffix", CLASS_SUFFIXES)
    def test_transform_returns_non_dict_input_unchanged(self, mod, suffix):
        module, idx = mod
        cls = getattr(module, f"LegCOR{idx}{suffix}")
        obj = cls()
        assert obj._t([1, 2, 3]) == [1, 2, 3]
        assert obj._t("plain-string") == "plain-string"


class TestWorkerThreadSelfTerminates:
    """
    Regression test for the specific undefined-name bug in the background
    thread: it should never hang or loop forever. Because every iteration of
    the try block raises before `self.__me["e"]` related bookkeeping is able
    to succeed via the normal path, the loop's own error budget (>10) causes
    it to exit almost immediately.
    """

    @pytest.mark.parametrize("idx", CORE_MODULE_IDS, ids=CORE_MODULE_IDS)
    def test_thread_exits_on_its_own_shortly_after_start(self, idx):
        module = load_module(idx)
        cls = getattr(module, f"LegCOR{idx}000")
        obj = cls()
        obj.start()
        try:
            thread = getattr(obj, f"_LegCOR{idx}000__th")
            thread.join(timeout=2)
            assert not thread.is_alive()
            error_counts = getattr(obj, f"_LegCOR{idx}000__me")
            assert error_counts["e"] > 10
            assert "p" not in error_counts
        finally:
            obj.stop()