from module import Controller,Usecase1
from unittest.mock import Mock,patch
import pytest

@patch.object(Usecase1,"execute",return_value="mock")
def test_patch_object(mock_exec):
    """
    Usage
        @patch.object(class,"attribute",return_value="hoge")
        def test_func(mock_method)

    理解
        patch.objectはあるクラスの特定のattribure(関数、変数)をモック化する。
        @patch.objectの場合、patchデコレートされたテスト内でパッチされた
        attributeを呼び出した場合、モックのreturn_valueで差し替えられる。
        mock_methodのassert_call系のメソッドを使うことで呼び出しを監視できる
    """
    controller=Controller(usecase1=Usecase1())
    assert controller.route_usecase1() == "mock"
    mock_exec.assert_called_once_with()

@patch('module.Usecase1',autospec=True)
def test_patch_autospec(mock_usecase_class):
    """
    Usage:
        @patch(target)
        def test_func(mock):
            statment
            ...
        
    理解
        patchを使うとtargetに指定したクラス自体をmockクラスにする
        関数の引数にmockクラスを指定する。

        指定したクラスのメソッドのreturn_valueをコントロールしたい場合、
        ①mockクラスからインスタンスを作成
        ②インスタンスのメソッドのreturn_valueを変更
        ③作成したインスタンスを使って、依存クラスを作成するなどして利用

        # autospec設定すると、モックにした元のクラスのメソッド(spec)を引き継ぐ。
        # 存在しないメソッドを使用しようとするとエラーになる。
        # クラスの変更があった場合に検知できるようになる。

    """
    a = Mock()
    a.execute
    # モックにはメソッドが自動追加されるので、エラーが起きない
    a.exec
    
    # mock_usecase.exec

    #mock_usecase.execute.return_value="mock"
    #controller=Controller(usecase1=Usecase1())
    #assert controller.route_usecase1() == "mock"
    #mock_usecase.assert_called_once_with()

    # ①mockClassからインスタンス作成
    mock_instance=mock_usecase_class.return_value
    
    # ②executeの返り値を変更
    mock_instance.execute.return_value="mock"
    
    # ③作成したインスタンスを使って依存クラスを作成
    controller=Controller(usecase1=mock_instance)
    # 挙動が意図しているかテスト
    assert controller.route_usecase1() == "mock"
    mock_instance.assert_called_once_with

    


