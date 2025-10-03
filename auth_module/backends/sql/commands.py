class SQLCommands:
    #######################
    #   User Management   #
    #######################
    ADD_USER = """
    -- ADD_USER
    INSERT INTO
      users (username, password_hash, role, disabled)
    values
      (%s, %s, %s, %s);
    """
    DELETE_USER = """
    -- DELETE_USER
    DELETE FROM users
    WHERE
      username = %s;
    """
    DISABLE_USER = """
    -- DISABLE_USER
    UPDATE users
    SET
      disabled = true
    WHERE
      username = %s;
    """
    ENABLE_USER = """
    -- ENABLE_USER
    UPDATE users
    SET
      disabled = false
    WHERE
      username = %s;
    """
    VALIDATE_USER = """
    -- VALIDATE_USER
    SELECT
      id,
      username,
      role,
      disabled
    FROM
      users
    WHERE
      username = %s
      AND password_hash = %s;
    """
    DESCRIBE_USER = """
    -- DESCRIBE_USER
    SELECT
      id,
      username,
      role,
      disabled
    FROM
      users
    WHERE
      username = %s;
    """

    #######################
    #   Table Management  #
    #######################

    ROLES = ["admin", "user", "guest"]

    USER_TABLE_CREATION = f"""
    -- USER_TABLE_CREATION
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        role VARCHAR(20) NOT NULL CHECK (role IN ('{"','".join(ROLES)}')),
        disabled BOOLEAN
    );
    """
    TOKEN_TABLE_CREATION = """
    -- TOKEN_TABLE_CREATION
    CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        token_hash VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP,
        active BOOLEAN DEFAULT TRUE
    );
    """
