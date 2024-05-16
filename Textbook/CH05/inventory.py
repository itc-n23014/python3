def display_inventory(inventory):
    print("持ち物リスト:\n" + "\n".join([f"{v} {k}" for k, v in inventory.items()]))
    print(f"アイテム総数: {sum([i for i in inventory.values()])}")

#メソッドとして使用するから、ファイルを指定
if __name__ == "__main__":
    a = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
    display_inventory(a)
