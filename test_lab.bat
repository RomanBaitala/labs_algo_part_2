@echo all test is running
python -m unittest discover

@REM or use this code to run specific tests

@REM @echo test1
@REM python -m unittest -v test/test_peek_sequence.py
@REM @echo test2
@REM python -m unittest -v test/test_max_dist_between_cows.py
@REM @echo test3
@REM python -m unittest -v test/test_max_diametr_in_bin_tree.py
@REM @echo test4
@REM python -m unittest -v test/test_red_black_priority_queue.py
@REM @echo test5
@REM python -m unittest -v test/test_find_the_number_of_islands.py
@REM @echo test6
@REM python -m unittest -v test/test_gas_supply_between_storage_facilities.py
@REM @echo test7
@REM python -m unittest -v test/test_max_flow_for_flower_shop.py
@REM @echo test8
@REM python -m unittest -v test/test_trie_tree.py
