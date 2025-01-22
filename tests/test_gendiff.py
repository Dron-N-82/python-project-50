from gendiff.generate_diff import maindiff

def test_main(mocker):
    mock = mocker.patch('gendiff.generate_diff.maindiff')
    
    from gendiff.scripts.gendiff import main
    main()
    mock.assert_called_once()