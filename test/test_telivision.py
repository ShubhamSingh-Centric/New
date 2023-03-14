from pytest import mark


def test_telivision_turns_on_2(tv_brand):
    tv_brand_name = tv_brand["brand"]
    tv_size = tv_brand["size"]
    print(f"\n{tv_brand_name} turns on as expected.")
    print(f"And {tv_brand_name} TV size is {tv_size} ")