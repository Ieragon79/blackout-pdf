# Blackout PDF - Architecture

## Overview

Blackout PDF is an offline desktop application designed to permanently remove sensitive information from PDF documents using true PDF redaction.

The application follows a modular architecture, where each component has a single responsibility.

```
               User
                 │
                 ▼
          Graphical Interface
                 │
                 ▼
           PDF Loader
                 │
                 ▼
        Sensitive Data Detector
                 │
                 ▼
        Redaction Engine
                 │
                 ▼
        Verification Engine
                 │
                 ▼
          PDF Exporter
```

---

# Modules

## GUI

Responsible for all user interaction.

Responsibilities:

- Select PDF files
- Configure detection options
- Display progress
- Preview detected sensitive information
- Save the sanitized document

---

## PDF Loader

Responsible for opening and validating PDF files.

Responsibilities:

- Open local PDF
- Validate file format
- Read document metadata
- Extract page structure

---

## Detector

Responsible for locating sensitive information.

Examples:

- CPF
- RG
- CNPJ
- Email
- Phone
- Address
- Names
- PIX Keys

The detector never modifies the document.

It only identifies candidate regions.

---

## Redaction Engine

Responsible for permanently removing sensitive information.

Requirements:

- Use True PDF Redaction
- Never draw fake black rectangles
- Remove original content from the PDF
- Optionally paint the removed area black

---

## Verification Engine

Responsible for validating the output.

Checks include:

- Extract remaining text
- Search for removed information
- Validate successful redaction
- Generate verification report

---

## Exporter

Responsible for generating the final document.

Responsibilities:

- Save sanitized PDF
- Preserve formatting whenever possible
- Remove temporary objects
- Optimize output

---

# Design Principles

- Offline First
- Open Source
- Privacy by Design
- True Redaction Only
- Simple User Experience
- Auditable Code
