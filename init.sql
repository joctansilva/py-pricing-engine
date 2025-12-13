CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE
    IF NOT EXISTS products (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4 (),
        code VARCHAR(20) UNIQUE NOT NULL,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP default NOW ()
    );

INSERT INTO
    products (code, name, description)
VALUES
    (
        'VIDA',
        'Seguro de Vida',
        'Cobertura por morte, invalidez e doenças graves.'
    ) (
        'AUTO',
        'Seguro de Automóvel',
        'Cobertura compreensiva, terceiros e assistencia'
    ) (
        'SAUDE',
        'Plano de Saúde',
        'Cobertura ambulatoria, hospitalar e laboratorial'
    ) ON CONFLICT DO NOTHING;

CREATE TABLE
    IF NOT EXISTS pricing_rules (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4 (),
        product_code VARCHAR(20) NOT NULL REFERENCES products (code),
        rule_type VARCHAR(100) NOT NULL,
        rule_name VARCHAR(200) NOT NULL,
        conditions JSONB NOT NULL DEFAULT '{}',
        value DECIMAL(10, 6) NOT NULL,
        value_type VARCHAR(20) DEFAULT 'MULTIPLIER',
        priority INT DEFAULT 0,
        valid_from DATE NOT NULL DEFAULT CURRENT_DATE,
        valid_until DATE,
        is_active BOOLEAN DEFAULT TRUE,
        created_by VARCHAR(100),
        created_at TIMESTAMP DEFAULT NOW (),
        updated_at TIMESTAMP DEFAULT NOW ()
    );

CREATE INDEX IF NOT EXISTS pricing_rules_lookup_idx ON pricing_rules (product_code, rule_type, valid_from, is_active);

CREATE INDEX IF NOT EXISTS pricing_rules_conditions_idx ON pricing_rules USING GIN (CONDITIONS);