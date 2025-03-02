"""
Simple Prompt Loader

A lightweight module for loading and rendering Jinja2 templates for prompts.
"""
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class PromptLoader:
    """Simple manager for prompt templates."""
    
    _env = None
    
    @classmethod
    def get_env(cls):
        """Get or create the Jinja2 environment."""
        if cls._env is None:
            # Assuming this file is in app/services/prompt_loader.py
            # and templates are in app/prompts/templates/
            current_file = Path(__file__)
            app_dir = current_file.parent.parent  # Go up to the app directory
            templates_dir = app_dir / "prompts" / "templates"
            
            # Print for debugging
            print(f"Loading templates from: {templates_dir}")
            
            cls._env = Environment(loader=FileSystemLoader(templates_dir))
        return cls._env
    
    @classmethod
    def render_prompt(cls, template_name, **kwargs):
        """Render a prompt template with the given variables.
        
        Args:
            template_name: Name of the template file (without .j2 extension)
            **kwargs: Variables to use in template rendering
            
        Returns:
            Rendered template string
        """
        env = cls.get_env()
        template = env.get_template(f"{template_name}.j2")
        return template.render(**kwargs)
    
#---------------------------------------------------------------------------
#
#                           below is what dave had
#
#---------------------------------------------------------------------------
    
# from pathlib import Path
# import frontmatter
# from jinja2 import Environment, FileSystemLoader, StrictUndefined, TemplateError, meta

# """
# Prompt Management Module

# This module provides functionality for loading and rendering prompt templates with frontmatter.
# It uses Jinja2 for template rendering and python-frontmatter for metadata handling,
# implementing a singleton pattern for template environment management.
# """


# class PromptManager:
#     """Manager class for handling prompt templates and their metadata.

#     This class provides functionality to load prompt templates from files,
#     render them with variables, and extract template metadata and requirements.
#     It implements a singleton pattern for the Jinja2 environment to ensure
#     consistent template loading across the application.

#     Attributes:
#         _env: Class-level singleton instance of Jinja2 Environment

#     Example:
#         # Render a prompt template with variables
#         prompt = PromptManager.get_prompt("rag_system_prompt", context_text="Some context")

#         # Get template metadata and required variables
#         info = PromptManager.get_template_info("rag_system_prompt")
#     """

#     _env = None

#     @classmethod
#     def _get_env(cls, templates_dir="prompts/templates") -> Environment:
#         """Gets or creates the Jinja2 environment singleton.

#         Args:
#             templates_dir: Directory name containing prompt templates, relative to app/

#         Returns:
#             Configured Jinja2 Environment instance

#         Note:
#             Uses StrictUndefined to raise errors for undefined variables,
#             helping catch template issues early.
#         """
#         templates_dir = Path(__file__).parent.parent / templates_dir
#         if cls._env is None:
#             cls._env = Environment(
#                 loader=FileSystemLoader(templates_dir),
#                 undefined=StrictUndefined,
#             )
#         return cls._env

#     @staticmethod
#     def get_prompt(template: str, **kwargs) -> str:
#         """Loads and renders a prompt template with provided variables.

#         Args:
#             template: Name of the template file (without .j2 extension)
#             **kwargs: Variables to use in template rendering

#         Returns:
#             Rendered template string

#         Raises:
#             ValueError: If template rendering fails
#             FileNotFoundError: If template file doesn't exist
#         """
#         env = PromptManager._get_env()
#         template_path = f"{template}.j2"
        
#         try:
#             # First try to load as a frontmatter file
#             with open(env.loader.get_source(env, template_path)[1]) as file:
#                 content = file.read()
                
#             # Check if the file has frontmatter
#             if content.startswith('---'):
#                 post = frontmatter.loads(content)
#                 template_content = post.content
#             else:
#                 # If no frontmatter, use the entire file content
#                 template_content = content
                
#             template = env.from_string(template_content)
#             return template.render(**kwargs)
#         except TemplateError as e:
#             raise ValueError(f"Error rendering template: {str(e)}")
#         except Exception as e:
#             raise ValueError(f"Error loading template: {str(e)}")

#     @staticmethod
#     def get_template_info(template: str) -> dict:
#         """Extracts metadata and variable requirements from a template.

#         Args:
#             template: Name of the template file (without .j2 extension)

#         Returns:
#             Dictionary containing:
#                 - name: Template name
#                 - description: Template description from frontmatter
#                 - author: Template author from frontmatter
#                 - variables: List of required template variables
#                 - frontmatter: Raw frontmatter metadata dictionary

#         Raises:
#             FileNotFoundError: If template file doesn't exist
#         """
#         env = PromptManager._get_env()
#         template_path = f"{template}.j2"
        
#         try:
#             with open(env.loader.get_source(env, template_path)[1]) as file:
#                 content = file.read()
                
#             # Check if the file has frontmatter
#             if content.startswith('---'):
#                 post = frontmatter.loads(content)
#                 template_content = post.content
#                 metadata = post.metadata
#             else:
#                 # If no frontmatter, use the entire file content
#                 template_content = content
#                 metadata = {}
                
#             ast = env.parse(template_content)
#             variables = meta.find_undeclared_variables(ast)

#             return {
#                 "name": template,
#                 "description": metadata.get("description", "No description provided"),
#                 "author": metadata.get("author", "Unknown"),
#                 "variables": list(variables),
#                 "frontmatter": metadata,
#             }
#         except Exception as e:
#             raise ValueError(f"Error analyzing template: {str(e)}")
