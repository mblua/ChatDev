---
title: MuleSoft API-led Application Blueprint Template
purpose: Instantiable template for generating standardized MuleSoft applications following the API-led Connectivity pattern.
audience: [architect, developer]
scope: Scaffolding for MuleSoft 4.x applications with built-in best practices for AI generation.
last_updated: 2026-01-12
version: 1.0.0
keywords: [mulesoft, template, api-led, scaffold, generation, blueprint]
---

# MuleSoft API-led Application Blueprint Template

## AI Agent Instructions

**Role**: You are a MuleSoft Expert Developer.
**Task**: Use this template to scaffold a new MuleSoft project based on user inputs.

### Generation Workflow:
1. **Gather Requirements**: Present the "User Questionnaire" to the user.
2. **Validate Input**: Ensure all required fields are provided.
3. **Generate Scaffolding**: Create the project folder structure and the XML files defined in the "Code Skeletons" section.
4. **Apply Best Practices**: Ensure the output follows the naming conventions and architectural rules defined in the repository.

---

## User Questionnaire

AI: Please ask the user these questions before generating the code:

1. **API Name**: (e.g., `customers-sapi`, `orders-papi`)
2. **API Layer**: (System, Process, or Experience)
3. **API Specification**: (RAML or OAS location/content)
4. **Backend Type**: (e.g., Salesforce, Database, SAP, REST API)
5. **Security Requirements**: (e.g., Client ID Enforcement, Basic Auth, OAuth 2.0)
6. **Persistence**: (e.g., Object Store, Database)
7. **Testing Threshold**: (Target MUnit coverage percentage)

---

## Project Structure (Conceptual)

```text
{{API_NAME}}/
├── src/main/mule/
│   ├── global.xml          # Global configurations and error handling
│   ├── interface.xml       # APIKit Router and listeners
│   └── implementation.xml  # Business logic flows
├── src/main/resources/
│   ├── api/                # API Specification files
│   └── config/             # YAML configuration files (dev, prod)
├── src/test/munit/         # MUnit test suites
└── pom.xml                 # Maven configuration
```

---

## Code Skeletons

### 1. global.xml
Contains shared configurations.

```xml
<mule xmlns:http="http://www.mulesoft.org/schema/mule/http" ...>
    <!-- HTTP Listener Config -->
    <http:listener-config name="HTTP_Listener_config">
        <http:listener-connection host="0.0.0.0" port="${http.port}" />
    </http:listener-config>

    <!-- Global Error Handler -->
    <error-handler name="global-error-handler">
        <on-error-propagate type="ANY">
            <set-payload value="#[output application/json --- {message: error.description}]" />
        </on-error-propagate>
    </error-handler>

    <configuration-properties file="config/config-${mule.env}.yaml" />
</mule>
```

### 2. interface.xml
Auto-generated from the API specification using APIKit.

```xml
<flow name="{{API_NAME}}-main">
    <http:listener config-ref="HTTP_Listener_config" path="/api/*">
        <http:response statusCode="#[vars.httpStatus default 200]" />
    </http:listener>
    <apikit:router config-ref="{{API_NAME}}-config" />
    <error-handler ref="global-error-handler" />
</flow>
```

### 3. implementation.xml
Where the business logic resides.

```xml
<flow name="get-{{RESOURCE}}-implementation">
    <logger level="INFO" message="Starting implementation for {{RESOURCE}}" />
    <!-- AI: Insert backend connector logic here based on Backend Type -->
</flow>
```

---

## AI Implementation Rules

1. **Naming Conventions**: Use `kebab-case` for file names and `camelCase` for variable names.
2. **Error Handling**: Every flow must reference the `global-error-handler` or have a local strategy.
3. **DataWeave**: Use explicit mappings. Avoid `*` selectors.
4. **Mocking**: Generate MUnit skeletons that mock the identified Backend Type.
5. **Security**: If "Client ID Enforcement" is chosen, include the appropriate policy header checks in the RAML/Flow.

---

## Compliance Checklist for AI

- [ ] Is the `API Name` used consistently?
- [ ] Does `global.xml` contain all shared properties?
- [ ] Is there a clear separation between `interface` and `implementation`?
- [ ] Are sensitive values placeholder-ed for Secure Properties?
- [ ] Are MUnit tests generated for the main success paths?
