"""add initial models

Revision ID: 87689d9b7669
Revises:
Create Date: 2025-06-24 08:15:30.565983+00:00

🚧 SMITHY MIGRATION 🚧
This file was automatically forged by Alembic.
Edit only if you know what you're doing.
"""

from typing import Sequence, Union

from alembic import op  # type: ignore
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "87689d9b7669"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "organizations",
        sa.Column(
            "name", sa.String(length=200), nullable=False, comment="Organization name"
        ),
        sa.Column(
            "slug",
            sa.String(length=50),
            nullable=False,
            comment="URL-friendly organization identifier",
        ),
        sa.Column(
            "display_name",
            sa.String(length=250),
            nullable=True,
            comment="Public display name (can be different from name)",
        ),
        sa.Column(
            "description", sa.Text(), nullable=True, comment="Organization description"
        ),
        sa.Column(
            "logo_url",
            sa.String(length=500),
            nullable=True,
            comment="Organization logo URL",
        ),
        sa.Column(
            "avatar_url",
            sa.String(length=500),
            nullable=True,
            comment="Organization avatar URL",
        ),
        sa.Column(
            "banner_url",
            sa.String(length=500),
            nullable=True,
            comment="Organization banner/cover URL",
        ),
        sa.Column(
            "brand_color",
            sa.String(length=7),
            nullable=True,
            comment="Primary brand color (hex)",
        ),
        sa.Column(
            "website_url",
            sa.String(length=500),
            nullable=True,
            comment="Organization website",
        ),
        sa.Column(
            "contact_email",
            sa.String(length=255),
            nullable=True,
            comment="Contact email address",
        ),
        sa.Column(
            "timezone",
            sa.String(length=50),
            nullable=True,
            comment="Organization timezone",
        ),
        sa.Column(
            "org_type",
            sa.Enum(
                "STARTUP",
                "SMALL_BUSINESS",
                "ENTERPRISE",
                "NON_PROFIT",
                "FREELANCER",
                "AGENCY",
                "PERSONAL",
                name="organizationtype",
            ),
            nullable=False,
            comment="Organization type",
        ),
        sa.Column(
            "company_size",
            sa.Enum(
                "SMALL",
                "MEDIUM",
                "LARGE",
                "ENTERPRISE",
                "SOLO",
                name="organizationsize",
            ),
            nullable=False,
            comment="Size of the organization",
        ),
        sa.Column(
            "max_members",
            sa.Integer(),
            nullable=False,
            comment="Maximum number of members allowed",
        ),
        sa.Column(
            "max_projects",
            sa.Integer(),
            nullable=False,
            comment="Maximum number of projects allowed",
        ),
        sa.Column(
            "max_storage_gb",
            sa.Integer(),
            nullable=False,
            comment="Maximum storage in GB",
        ),
        sa.Column(
            "settings", sa.JSON(), nullable=True, comment="Organization configuration"
        ),
        sa.Column(
            "features",
            sa.JSON(),
            nullable=True,
            comment="Enabled features and feature flags",
        ),
        sa.Column(
            "integrations",
            sa.JSON(),
            nullable=True,
            comment="External integrations configuration",
        ),
        sa.Column(
            "require_2fa",
            sa.Boolean(),
            nullable=False,
            comment="Require 2FA for all members",
        ),
        sa.Column(
            "public_projects",
            sa.Boolean(),
            nullable=False,
            comment="Allow public project visibility",
        ),
        sa.Column(
            "deleted_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Soft deletion timestamp",
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint(
            "brand_color IS NULL OR brand_color ~ '^#[0-9A-Fa-f]{6}$'",
            name="valid_brand_color",
        ),
        sa.CheckConstraint("slug ~ '^[a-z0-9-]+$'", name="org_slug_format"),
        sa.CheckConstraint(
            "LENGTH(slug) >= 2 AND LENGTH(slug) <= 50", name="org_slug_length"
        ),
        sa.CheckConstraint("max_members > 0", name="positive_max_members"),
        sa.CheckConstraint("max_projects > 0", name="positive_max_projects"),
        sa.CheckConstraint("max_storage_gb > 0", name="positive_max_storage"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("slug", name="unique_org_slug"),
    )
    op.create_index(
        "idx_org_slug_active", "organizations", ["slug", "deleted_at"], unique=False
    )
    op.create_index(
        "idx_org_type_size", "organizations", ["org_type", "company_size"], unique=False
    )
    op.create_index(
        op.f("ix_organizations_company_size"),
        "organizations",
        ["company_size"],
        unique=False,
    )
    op.create_index(
        op.f("ix_organizations_deleted_at"),
        "organizations",
        ["deleted_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_organizations_org_type"), "organizations", ["org_type"], unique=False
    )
    op.create_index(
        op.f("ix_organizations_slug"), "organizations", ["slug"], unique=True
    )
    op.create_table(
        "users",
        sa.Column(
            "email",
            sa.String(length=255),
            nullable=False,
            comment="User's email address",
        ),
        sa.Column(
            "username", sa.String(length=50), nullable=False, comment="User's username"
        ),
        sa.Column(
            "password_hash",
            sa.String(length=255),
            nullable=True,
            comment="Hashed password for authentication (null if using external auth)",
        ),
        sa.Column(
            "login_provider",
            sa.String(length=50),
            nullable=False,
            comment="Authentication provider used for login",
        ),
        sa.Column(
            "first_name",
            sa.String(length=191),
            nullable=True,
            comment="User's first name",
        ),
        sa.Column(
            "last_name",
            sa.String(length=191),
            nullable=True,
            comment="User's last name",
        ),
        sa.Column(
            "display_name",
            sa.String(length=191),
            nullable=True,
            comment="User's display name (if different from username)",
        ),
        sa.Column(
            "bio",
            sa.Text(),
            nullable=True,
            comment="Short biography or description of the user",
        ),
        sa.Column(
            "timezone",
            sa.String(length=50),
            nullable=True,
            comment="User's preferred timezone in IANA format",
        ),
        sa.Column(
            "locale",
            sa.String(length=10),
            nullable=True,
            comment="User's preferred locale (e.g., en-US)",
        ),
        sa.Column(
            "status",
            sa.Enum(
                "ACTIVE",
                "INACTIVE",
                "SUSPENDED",
                "PENDING_VERIFICATION",
                "ARCHIVED",
                name="userstatus",
                native_enum=False,
            ),
            nullable=False,
            comment="Current status of the user account",
        ),
        sa.Column(
            "role",
            sa.Enum("ADMIN", "MODERATOR", "USER", "GUEST", name="userrole"),
            nullable=False,
            comment="Role of the user for access control",
        ),
        sa.Column(
            "is_verified",
            sa.Boolean(),
            nullable=False,
            comment="Indicates if the user's email is verified",
        ),
        sa.Column(
            "is_superuser",
            sa.Boolean(),
            nullable=False,
            comment="Indicates if the user has superuser privileges",
        ),
        sa.Column(
            "mfa_enabled",
            sa.Boolean(),
            nullable=False,
            comment="Indicates if multi-factor authentication is enabled",
        ),
        sa.Column(
            "mfa_secret",
            sa.String(length=255),
            nullable=True,
            comment="TOTP secret for MFA",
        ),
        sa.Column(
            "failed_login_attempts",
            sa.Integer(),
            nullable=False,
            comment="Consecutive failed login attempts",
        ),
        sa.Column(
            "oauth_accounts",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
            comment="Connected OAuth accounts data",
        ),
        sa.Column(
            "external_id",
            sa.String(length=255),
            nullable=True,
            comment="External system user ID",
        ),
        sa.Column(
            "last_login_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Last successful login timestamp",
        ),
        sa.Column(
            "last_activity_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Last activity timestamp",
        ),
        sa.Column(
            "login_count", sa.Integer(), nullable=False, comment="Total login count"
        ),
        sa.Column(
            "email_verification_token",
            sa.String(length=255),
            nullable=True,
            comment="Email verification token",
        ),
        sa.Column(
            "email_verification_expires",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Email verification token expiration",
        ),
        sa.Column(
            "password_reset_token",
            sa.String(length=255),
            nullable=True,
            comment="Password reset token",
        ),
        sa.Column(
            "password_reset_expires",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Password reset token expiration",
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint(
            "email ~* '^[A-Za-z0-9._%%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'",
            name="valid_email_format",
        ),
        sa.CheckConstraint(
            "LENGTH(username) >= 3 OR username IS NULL", name="username_min_length"
        ),
        sa.CheckConstraint("login_count >= 0", name="non_negative_login_count"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email_verification_token"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("password_reset_token"),
    )
    op.create_index(
        "idx_user_created_status", "users", ["created_at", "status"], unique=False
    )
    op.create_index("idx_user_email_status", "users", ["email", "status"], unique=False)
    op.create_index(
        "idx_user_last_activity", "users", ["last_activity_at"], unique=False
    )
    op.create_index("idx_user_role_status", "users", ["role", "status"], unique=False)
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(
        op.f("ix_users_external_id"), "users", ["external_id"], unique=False
    )
    op.create_index(
        op.f("ix_users_last_activity_at"), "users", ["last_activity_at"], unique=False
    )
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=True)
    op.create_table(
        "mfa_backup_codes",
        sa.Column(
            "user_id",
            sa.UUID(),
            nullable=False,
            comment="User who owns this backup code",
        ),
        sa.Column(
            "code_hash",
            sa.String(length=255),
            nullable=False,
            comment="Hashed backup code",
        ),
        sa.Column(
            "is_used",
            sa.Boolean(),
            nullable=False,
            comment="Whether this backup code has been used",
        ),
        sa.Column(
            "used_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="When this backup code was used",
        ),
        sa.Column(
            "used_from_ip",
            sa.String(length=45),
            nullable=True,
            comment="IP address from which the code was used",
        ),
        sa.Column(
            "generated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            comment="When this backup code was generated",
        ),
        sa.Column(
            "expires_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="When this backup code expires (optional)",
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_index(
        "idx_mfa_backup_expires", "mfa_backup_codes", ["expires_at"], unique=False
    )
    op.create_index(
        "idx_mfa_backup_generated", "mfa_backup_codes", ["generated_at"], unique=False
    )
    op.create_index(
        "idx_mfa_backup_user_active",
        "mfa_backup_codes",
        ["user_id", "is_used"],
        unique=False,
    )
    op.create_index(
        op.f("ix_mfa_backup_codes_user_id"),
        "mfa_backup_codes",
        ["user_id"],
        unique=False,
    )
    op.create_table(
        "organization_members",
        sa.Column("user_id", sa.UUID(), nullable=False, comment="User ID"),
        sa.Column(
            "organization_id", sa.UUID(), nullable=False, comment="Organization ID"
        ),
        sa.Column(
            "role",
            sa.Enum(
                "OWNER",
                "ADMIN",
                "MANAGER",
                "MEMBER",
                "VIEWER",
                "GUEST",
                name="organizationrole",
            ),
            nullable=False,
            comment="Member role within organization",
        ),
        sa.Column(
            "status",
            sa.Enum("ACTIVE", "PENDING", "SUSPENDED", "LEFT", name="memberstatus"),
            nullable=False,
            comment="Member status",
        ),
        sa.Column(
            "invited_by",
            sa.UUID(),
            nullable=True,
            comment="User who invited this member",
        ),
        sa.Column(
            "invited_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Invitation timestamp",
        ),
        sa.Column(
            "joined_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="When member accepted invitation",
        ),
        sa.Column(
            "last_active_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Last activity in organization",
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["invited_by"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("user_id", "organization_id", name="unique_user_org"),
    )
    op.create_index(
        "idx_org_member_role",
        "organization_members",
        ["organization_id", "role"],
        unique=False,
    )
    op.create_index(
        "idx_org_member_status",
        "organization_members",
        ["organization_id", "status"],
        unique=False,
    )
    op.create_index(
        "idx_user_orgs_active",
        "organization_members",
        ["user_id", "status"],
        unique=False,
    )
    op.create_index(
        op.f("ix_organization_members_role"),
        "organization_members",
        ["role"],
        unique=False,
    )
    op.create_index(
        op.f("ix_organization_members_status"),
        "organization_members",
        ["status"],
        unique=False,
    )
    op.create_table(
        "projects",
        sa.Column(
            "name", sa.String(length=200), nullable=False, comment="Project name"
        ),
        sa.Column(
            "key",
            sa.String(length=6),
            nullable=False,
            comment="Project key (e.g., PANEL, DASH) - max 6 chars, used for task IDs",
        ),
        sa.Column(
            "description", sa.Text(), nullable=True, comment="Project description"
        ),
        sa.Column(
            "organization_id",
            sa.UUID(),
            nullable=False,
            comment="Organization that owns this project",
        ),
        sa.Column(
            "lead_id",
            sa.UUID(),
            nullable=True,
            comment="Project lead/manager (must be org member)",
        ),
        sa.Column(
            "icon",
            sa.String(length=100),
            nullable=True,
            comment="Project icon (emoji, icon name, or URL)",
        ),
        sa.Column(
            "color",
            sa.String(length=7),
            nullable=True,
            comment="Project color theme (hex color)",
        ),
        sa.Column(
            "cover_image_url",
            sa.String(length=500),
            nullable=True,
            comment="Project cover image URL",
        ),
        sa.Column(
            "status",
            sa.Enum(
                "PLANNING",
                "ACTIVE",
                "ON_HOLD",
                "COMPLETED",
                "ARCHIVED",
                "CANCELLED",
                name="projectstatus",
            ),
            nullable=False,
            comment="Current project status",
        ),
        sa.Column(
            "priority",
            sa.Enum("LOW", "MEDIUM", "HIGH", "CRITICAL", name="projectpriority"),
            nullable=False,
            comment="Project priority level",
        ),
        sa.Column(
            "visibility",
            sa.Enum("PRIVATE", "ORGANIZATION", "PUBLIC", name="projectvisibility"),
            nullable=False,
            comment="Project visibility settings",
        ),
        sa.Column(
            "start_date",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Project start date",
        ),
        sa.Column(
            "due_date",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Project due date",
        ),
        sa.Column(
            "completed_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Project completion timestamp",
        ),
        sa.Column(
            "enable_subtasks",
            sa.Boolean(),
            nullable=False,
            comment="Enable subtask creation",
        ),
        sa.Column(
            "settings",
            sa.JSON(),
            nullable=True,
            comment="Project configuration and settings",
        ),
        sa.Column(
            "archived_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Project archival timestamp",
        ),
        sa.Column(
            "deleted_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Soft deletion timestamp",
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint(
            "color IS NULL OR color ~ '^#[0-9A-Fa-f]{6}$'", name="valid_hex_color"
        ),
        sa.CheckConstraint("key ~ '^[A-Z][A-Z0-9]*$'", name="project_key_format"),
        sa.CheckConstraint(
            "LENGTH(key) >= 2 AND LENGTH(key) <= 6", name="project_key_length"
        ),
        sa.CheckConstraint(
            "start_date IS NULL OR due_date IS NULL OR start_date <= due_date",
            name="valid_date_range",
        ),
        sa.ForeignKeyConstraint(["lead_id"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint(
            "organization_id", "key", name="unique_project_key_per_org"
        ),
    )
    op.create_index(
        "idx_project_archived",
        "projects",
        ["archived_at", "organization_id"],
        unique=False,
    )
    op.create_index(
        "idx_project_dates", "projects", ["start_date", "due_date"], unique=False
    )
    op.create_index(
        "idx_project_lead_active", "projects", ["lead_id", "status"], unique=False
    )
    op.create_index(
        "idx_project_org_key", "projects", ["organization_id", "key"], unique=False
    )
    op.create_index(
        "idx_project_org_status",
        "projects",
        ["organization_id", "status"],
        unique=False,
    )
    op.create_index(
        "idx_project_visibility_public",
        "projects",
        ["visibility", "organization_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_projects_archived_at"), "projects", ["archived_at"], unique=False
    )
    op.create_index(
        op.f("ix_projects_deleted_at"), "projects", ["deleted_at"], unique=False
    )
    op.create_index(op.f("ix_projects_key"), "projects", ["key"], unique=False)
    op.create_index(op.f("ix_projects_lead_id"), "projects", ["lead_id"], unique=False)
    op.create_index(
        op.f("ix_projects_organization_id"),
        "projects",
        ["organization_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_projects_priority"), "projects", ["priority"], unique=False
    )
    op.create_index(op.f("ix_projects_status"), "projects", ["status"], unique=False)
    op.create_index(
        op.f("ix_projects_visibility"), "projects", ["visibility"], unique=False
    )
    op.create_table(
        "project_members",
        sa.Column("project_id", sa.UUID(), nullable=False, comment="Project ID"),
        sa.Column("user_id", sa.UUID(), nullable=False, comment="User ID"),
        sa.Column(
            "role",
            sa.Enum("LEAD", "DEVELOPER", "REVIEWER", "VIEWER", name="projectrole"),
            nullable=False,
            comment="Role within this project",
        ),
        sa.Column(
            "added_at",
            sa.DateTime(timezone=True),
            nullable=False,
            comment="When user was added to project",
        ),
        sa.Column(
            "added_by",
            sa.UUID(),
            nullable=True,
            comment="Who added this user to project",
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["added_by"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("project_id", "user_id", name="unique_project_member"),
    )
    op.create_index(
        "idx_project_members", "project_members", ["project_id", "role"], unique=False
    )
    op.create_index(
        "idx_user_projects", "project_members", ["user_id", "role"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("idx_user_projects", table_name="project_members")
    op.drop_index("idx_project_members", table_name="project_members")
    op.drop_table("project_members")
    op.drop_index(op.f("ix_projects_visibility"), table_name="projects")
    op.drop_index(op.f("ix_projects_status"), table_name="projects")
    op.drop_index(op.f("ix_projects_priority"), table_name="projects")
    op.drop_index(op.f("ix_projects_organization_id"), table_name="projects")
    op.drop_index(op.f("ix_projects_lead_id"), table_name="projects")
    op.drop_index(op.f("ix_projects_key"), table_name="projects")
    op.drop_index(op.f("ix_projects_deleted_at"), table_name="projects")
    op.drop_index(op.f("ix_projects_archived_at"), table_name="projects")
    op.drop_index("idx_project_visibility_public", table_name="projects")
    op.drop_index("idx_project_org_status", table_name="projects")
    op.drop_index("idx_project_org_key", table_name="projects")
    op.drop_index("idx_project_lead_active", table_name="projects")
    op.drop_index("idx_project_dates", table_name="projects")
    op.drop_index("idx_project_archived", table_name="projects")
    op.drop_table("projects")
    op.drop_index(
        op.f("ix_organization_members_status"), table_name="organization_members"
    )
    op.drop_index(
        op.f("ix_organization_members_role"), table_name="organization_members"
    )
    op.drop_index("idx_user_orgs_active", table_name="organization_members")
    op.drop_index("idx_org_member_status", table_name="organization_members")
    op.drop_index("idx_org_member_role", table_name="organization_members")
    op.drop_table("organization_members")
    op.drop_index(op.f("ix_mfa_backup_codes_user_id"), table_name="mfa_backup_codes")
    op.drop_index("idx_mfa_backup_user_active", table_name="mfa_backup_codes")
    op.drop_index("idx_mfa_backup_generated", table_name="mfa_backup_codes")
    op.drop_index("idx_mfa_backup_expires", table_name="mfa_backup_codes")
    op.drop_table("mfa_backup_codes")
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.drop_index(op.f("ix_users_last_activity_at"), table_name="users")
    op.drop_index(op.f("ix_users_external_id"), table_name="users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_index("idx_user_role_status", table_name="users")
    op.drop_index("idx_user_last_activity", table_name="users")
    op.drop_index("idx_user_email_status", table_name="users")
    op.drop_index("idx_user_created_status", table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_organizations_slug"), table_name="organizations")
    op.drop_index(op.f("ix_organizations_org_type"), table_name="organizations")
    op.drop_index(op.f("ix_organizations_deleted_at"), table_name="organizations")
    op.drop_index(op.f("ix_organizations_company_size"), table_name="organizations")
    op.drop_index("idx_org_type_size", table_name="organizations")
    op.drop_index("idx_org_slug_active", table_name="organizations")
    op.drop_table("organizations")
    # ### end Alembic commands ###
