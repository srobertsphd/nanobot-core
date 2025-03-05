from app.config.settings import settings

def test_settings_loaded():
    """Test that settings are loaded correctly."""
    # Check OpenAI settings
    assert hasattr(settings, 'openai')
    assert hasattr(settings.openai, 'api_key')
    assert hasattr(settings.openai, 'embedding_model')
    assert hasattr(settings.openai, 'embedding_dimensions')
    
    # Check database settings - using local_db instead of database
    assert hasattr(settings, 'local_db')
    assert hasattr(settings.local_db, 'host')
    assert hasattr(settings.local_db, 'port')
    assert hasattr(settings.local_db, 'name')
    
    # Check admin database settings
    assert hasattr(settings, 'admin_db')
    
    # Check vector index settings
    assert hasattr(settings, 'vector_index')
    assert hasattr(settings.vector_index, 'index_type')
