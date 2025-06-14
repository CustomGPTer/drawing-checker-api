qa_checks = {
    "cover_invert_levels": {
        "description": "Cover and invert levels shown at every manhole or pipe run",
        "category": "Civils",
        "CESWI": "Clause 505.3.1",
        "UUCESWI": "Clause 505.3.1 – All manholes must show cover and invert levels",
        "BestPractice": "Show both IL (invert level) and CL (cover level) on plan and section views",
        "diagnostic": {
            "likely_cause": "Invert or cover level annotation omitted or on wrong layer",
            "risk": "Incorrect excavation depth or pipe fall leading to build errors",
            "fix": [
                "Label IL and CL at every chamber and pipe end",
                "Ensure invert levels are on a visible layer or style"
            ]
        }
    },
    "pipe_bedding": {
        "description": "Correct pipe bedding type specified and shown",
        "category": "Civils",
        "CESWI": "Clause 505.3.1",
        "UUCESWI": "Addendum A – Type B bedding required under roads",
        "BestPractice": "Reference UU standard detail 6101 or CIRIA C689 for bedding",
        "diagnostic": {
            "likely_cause": "Bedding note or section omitted",
            "risk": "Incorrect bedding leads to pipe deformation or failure",
            "fix": [
                "Include general note 'Pipe bedding per CESWI Type B'",
                "Add a typical bedding detail section or note"
            ]
        }
    },
    "flow_direction": {
        "description": "Flow direction clearly indicated along all pipe runs",
        "category": "Civils",
        "CESWI": "Clause 502.1.2",
        "UUCESWI": "Noted in CESWI Section 5 – flow direction arrows required",
        "BestPractice": "Place arrows every 10–15m along the pipe run on plan",
        "diagnostic": {
            "likely_cause": "Flow arrows not inserted or layer turned off",
            "risk": "Incorrect pipe fall direction during install causing flow issues",
            "fix": [
                "Add flow direction arrows on plan and section views",
                "Use a dedicated layer for flow arrows"
            ]
        }
    },
    "chamber_references": {
        "description": "Chamber references match layout and manhole schedule",
        "category": "Civils",
        "CESWI": "Clause 505.4.1",
        "UUCESWI": "Match manhole numbering to MH schedule",
        "BestPractice": "Use unique manhole IDs on plan, section, and schedule",
        "diagnostic": {
            "likely_cause": "Mismatch between drawing and MH schedule references",
            "risk": "Wrong chamber constructed in wrong location",
            "fix": [
                "Verify chamber IDs align with MH schedule and site plan",
                "Correct any discrepancies between drawing and schedule"
            ]
        }
    },
    "wall_slab_thickness": {
        "description": "Wall, slab, and foundation thicknesses are shown and labelled",
        "category": "Civils",
        "CESWI": "Clause 505.5.1",
        "UUCESWI": "Refer to structural detail notes in civils package",
        "BestPractice": "Label all wall, slab, and foundation thicknesses on drawings",
        "diagnostic": {
            "likely_cause": "Thicknesses omitted or inherited from generic template",
            "risk": "Structures may be under/over-designed or clash with other elements",
            "fix": [
                "Annotate thickness on section views and plan callouts",
                "Cross-check with structural drawings for consistency"
            ]
        }
    },
    "reinforcement_details": {
        "description": "Reinforcement details shown for slabs, walls, or concrete pads",
        "category": "Civils",
        "CESWI": "Clause 502.3.2",
        "UUCESWI": "Refer to RC detailing notes in civils package",
        "BestPractice": "Use B-series rebar callouts and show bar schedules on drawings",
        "diagnostic": {
            "likely_cause": "Missing bar marks or reinforcement overlay in CAD",
            "risk": "Incorrect rebar placement or quantity causing structural issues",
            "fix": [
                "Add rebar layout with bar marks and spacing notes",
                "Include reference to bar schedule for each element"
            ]
        }
    },
    "pipe_sizes_and_materials": {
        "description": "Pipe sizes, material, and jointing are clearly labelled",
        "category": "Civils",
        "CESWI": "Clause 505.2.1",
        "UUCESWI": "Use UU-approved materials (e.g., DI, uPVC)",
        "BestPractice": "Add callouts like 'Ø150 DI PN16 w/ flange joints' on plan",
        "diagnostic": {
            "likely_cause": "Generic pipe lines used with no annotation",
            "risk": "Wrong pipe type or joint may be used on site",
            "fix": [
                "Label each pipe with size, material, and joint type",
                "Ensure symbol legends match the annotated materials"
            ]
        }
    },
    "access_ladders": {
        "description": "Access ladders or platforms provided for deep chambers or structures",
        "category": "Civils",
        "CESWI": "Clause 509.4.3",
        "UUCESWI": "Comply with working-at-height procedures",
        "BestPractice": "Show permanent ladders for access >1.5m depth",
        "diagnostic": {
            "likely_cause": "Ladders/platforms omitted from drawing",
            "risk": "Unsafe entry or exit into deep chambers on site",
            "fix": [
                "Add fixed ladder to sections deeper than 1.2m",
                "Include platform or handhold detail where required"
            ]
        }
    },
    "maintenance_access": {
        "description": "Chambers, covers, and equipment are accessible for lifting and maintenance",
        "category": "Civils",
        "CESWI": "Clause 509.3.1",
        "UUCESWI": "Ensure 1m clearance around maintainable equipment",
        "BestPractice": "Maintain clear 1m zones around access hatches and equipment",
        "diagnostic": {
            "likely_cause": "Maintenance access not considered in layout",
            "risk": "Difficult or unsafe maintenance operations on site",
            "fix": [
                "Draw 1m clearance around maintainable equipment and hatches",
                "Add note 'Maintain clear access for operatives'"
            ]
        }
    },
    "views_coordinated": {
        "description": "Plan, section, and detail views are fully coordinated",
        "category": "Combined",
        "CESWI": "Clause 505.1.1",
        "UUCESWI": "Drawing views must be consistent and referenced",
        "BestPractice": "Cross-check dimensions and references between plan and section views",
        "diagnostic": {
            "likely_cause": "Separate drawings not aligned or missing coordination",
            "risk": "Dimensions or features may not match across views causing build errors",
            "fix": [
                "Align plan and section references (e.g., match lines, levels)",
                "Use view references and cross-hatching consistently"
            ]
        }
    },
    "cable_trays": {
        "description": "Cable tray routing shown, free of clashes and obstructions",
        "category": "Electrical",
        "CESWI": "Clause 512.1.1",
        "UUCESWI": "Cable trays must not obstruct access or vents",
        "BestPractice": "Use 90° bends and maintain max 3% incline, annotate in section",
        "diagnostic": {
            "likely_cause": "Tray layout deferred to contractor or not drawn",
            "risk": "Unbuildable cable runs or clashes with structure",
            "fix": [
                "Add plan and elevation for main tray routes",
                "Ensure adequate clearance under structural elements"
            ]
        }
    },
    "duct_spacing": {
        "description": "Cable duct layout and spacing are correctly shown",
        "category": "Electrical",
        "CESWI": "Clause 512.1.2",
        "UUCESWI": "Ducts to be spaced minimum 100mm apart",
        "BestPractice": "Show duct-bank layout and trench detail on plan",
        "diagnostic": {
            "likely_cause": "Single duct shown with no spacing detail",
            "risk": "Crowded ducts leading to installation difficulty",
            "fix": [
                "Annotate duct spacing and material sizes",
                "Include typical duct bank cross-section with spacing"
            ]
        }
    },
    "drawpits": {
        "description": "Drawpits and duct bends shown with required spacing and buildable layout",
        "category": "Electrical",
        "CESWI": "Clause 512.1.3",
        "UUCESWI": "Conform to UU standards for drawpit construction",
        "BestPractice": "Maintain at least 100mm clearance to walls and 300mm between HV and LV ducts",
        "diagnostic": {
            "likely_cause": "Drawpit geometry or duct bends not detailed",
            "risk": "Installers may not be able to form drawpits or route cables as intended",
            "fix": [
                "Add plan and section of typical drawpit",
                "Ensure bends and pull points are dimensioned and labelled"
            ]
        }
    },
    "pumps_equipment": {
        "description": "Pumps, valves, and mechanical equipment fully detailed and accessible",
        "category": "Mechanical",
        "CESWI": "Clause 508.2.1",
        "UUCESWI": "Locate valves to isolate major branches",
        "BestPractice": "Include manufacturer data and clearance zones for equipment",
        "diagnostic": {
            "likely_cause": "Equipment detail omitted or generic symbols used",
            "risk": "Incorrect equipment selection or inaccessible maintenance",
            "fix": [
                "Add equipment tags and detailed callouts for pumps and valves",
                "Verify maintenance clearance around each item"
            ]
        }
    },
    "isolation_points": {
        "description": "Electrical and mechanical isolation points clearly marked and labelled",
        "category": "Electrical",
        "CESWI": "Clause 512.5.2",
        "UUCESWI": "Show all isolation valves and switches for circuits",
        "BestPractice": "Use standard symbols and callouts for isolation devices",
        "diagnostic": {
            "likely_cause": "Isolation points not identified in drawing",
            "risk": "Maintenance tasks may require unexpected shutdowns or are unsafe",
            "fix": [
                "Add valves and switch symbols to drawings",
                "Label all isolation points with tag names"
            ]
        }
    },
    "sensor_positions": {
        "description": "Sensors, instruments, and probes located correctly and logically",
        "category": "Combined",
        "CESWI": "Clause 513.2.1",
        "UUCESWI": "Match sensor types to P&ID and field layout",
        "BestPractice": "Include probe depths and mounting details on drawings",
        "diagnostic": {
            "likely_cause": "Sensor locations not coordinated or generic",
            "risk": "Incorrect sensor placement leading to control issues",
            "fix": [
                "Mark sensor types (e.g., pH, flow, temperature) with callouts",
                "Confirm sensor heights and access requirements on plan"
            ]
        }
    },
    "control_panels": {
        "description": "Control panels coordinated with structure, access, and cabling",
        "category": "Electrical",
        "CESWI": "Clause 512.3.1",
        "UUCESWI": "No panel should obstruct routes or safety zones",
        "BestPractice": "Show panel outline and door swing with cable entry paths",
        "diagnostic": {
            "likely_cause": "Panel footprint not drawn or crowding other elements",
            "risk": "Cabling or access may require redesign on site",
            "fix": [
                "Add panel outlines to wall layouts with clearance zones",
                "Verify enough space for cable termination and user access"
            ]
        }
    },
    "civil_penetrations": {
        "description": "All M&E penetrations shown and coordinated with civils",
        "category": "Combined",
        "CESWI": "Clause 502.2.4",
        "UUCESWI": "All penetrations must be sleeved and waterproofed",
        "BestPractice": "Use standard sleeve sizes (twice pipe OD) and show on drawing",
        "diagnostic": {
            "likely_cause": "M&E routes not overlaid on civils drawing or missing sleeves",
            "risk": "Late coordination issues causing core drill or concrete breaks",
            "fix": [
                "Overlay M&E duct/pipe routes onto civil plans",
                "Add cast-in penetration details or notations"
            ]
        }
    },
    "vent_routes": {
        "description": "Vent and overflow routes logical, labelled, and clash-free",
        "category": "Mechanical",
        "CESWI": "Clause 508.4.1",
        "UUCESWI": "Overflows must not discharge to surface water",
        "BestPractice": "Mark vent and overflow pipe ends with labels in plan",
        "diagnostic": {
            "likely_cause": "Vent/overflow routes not defined or coordinated",
            "risk": "Discharge into wrong system or asset clashes causing backflow",
            "fix": [
                "Ensure overflow connects to correct drain or return system",
                "Add air valve and vent point details with labels"
            ]
        }
    },
    "bonding_earthing": {
        "description": "Earthing, bonding, and lightning protection shown and compliant",
        "category": "Electrical",
        "CESWI": "Clause 512.5.1",
        "UUCESWI": "See WIMES 1.02 for bonding and earthing requirements",
        "BestPractice": "Bond all metallic pipes, tanks, cable trays, and support steel",
        "diagnostic": {
            "likely_cause": "Earthing details not included in M&E drawings",
            "risk": "Electrical hazards or non-compliance with regulations",
            "fix": [
                "Add earthing/bonding symbols to relevant assets",
                "Include schematic or notes of bonding system"
            ]
        }
    },
    "standards_compliance": {
        "description": "Drawing complies with relevant CESWI/UUCESWI or WIMES standards",
        "category": "General",
        "CESWI": "Clause 130.5.2",
        "UUCESWI": "All drawings should meet CESWI and WIMES requirements",
        "BestPractice": "List applicable standards in general notes or title block",
        "diagnostic": {
            "likely_cause": "Standards compliance not checked or documented",
            "risk": "Drawing may violate design/specification requirements",
            "fix": [
                "Review drawing against CESWI, UUCESWI, and WIMES checklists",
                "Add note confirming compliance with relevant standards"
            ]
        }
    },
    "standard_details": {
        "description": "United Utilities standard detail references are correctly applied",
        "category": "General",
        "CESWI": "Clause 505.1.1",
        "UUCESWI": "All construction details must match UU standard references",
        "BestPractice": "Use STD codes (e.g., STD6101) in callouts or notes",
        "diagnostic": {
            "likely_cause": "Generic or outdated detail references used",
            "risk": "Non-compliant construction details causing inspection failures",
            "fix": [
                "Update all detail callouts to current UU STD numbers",
                "Include notes like 'See UU STD XXXX for detail'"
            ]
        }
    },
    "current_revision": {
        "description": "Drawing is the current approved-for-construction revision",
        "category": "General",
        "CESWI": "Clause 130.1.4",
        "UUCESWI": "Only the current FOR CONSTRUCTION issue may be used on site",
        "BestPractice": "Show revision and issue date on all title blocks and notes",
        "diagnostic": {
            "likely_cause": "Title block not updated or drawing version mismatched",
            "risk": "Outdated design issued to site causing rework or errors",
            "fix": [
                "Confirm latest revision with document control",
                "Clearly mark FOR CONSTRUCTION on current issue drawings"
            ]
        }
    },
    "referenced_drawings": {
        "description": "Referenced drawings are listed and up to date",
        "category": "General",
        "CESWI": "Clause 130.6.1",
        "UUCESWI": "All drawings must show up-to-date references",
        "BestPractice": "Include drawing reference list in title block or notes",
        "diagnostic": {
            "likely_cause": "Drawing index not maintained during revisions",
            "risk": "Construction based on outdated or missing drawings",
            "fix": [
                "Add or update drawing reference list on the drawing",
                "Cross-check against the issue register for latest drawings"
            ]
        }
    },
    "temporary_works": {
        "description": "Notes on temporary works (shoring, phasing) are included if required",
        "category": "General",
        "CESWI": "Clause 130.4.1",
        "UUCESWI": "Temporary works required for excavations >1.2m or unstable ground",
        "BestPractice": "Add note 'TW design by others' or include typical shoring detail",
        "diagnostic": {
            "likely_cause": "Temporary works not considered in design drawings",
            "risk": "Unsafe excavation or collapse during construction",
            "fix": [
                "Add general note on temporary works requirements",
                "Include typical shoring or bracing details if applicable"
            ]
        }
    },
    "safety_zones": {
        "description": "Maintenance zones, lifting areas, and fall protection are clearly shown",
        "category": "Combined",
        "CESWI": "Clause 509.5.2",
        "UUCESWI": "Exclusion zones required around lifting operations",
        "BestPractice": "Mark lifting envelopes and guardrail lines on plan",
        "diagnostic": {
            "likely_cause": "Lifting/fall protection planning not included in drawing",
            "risk": "Unsafe lifting operations or unprotected edges during construction",
            "fix": [
                "Add dashed lines for crane swing areas and clear zones",
                "Include notes on required guardrails and harness anchor points"
            ]
        }
    },
    "scope_definition": {
        "description": "Scope of work clearly defined in title block and general notes",
        "category": "General",
        "CESWI": "Clause 130.2.2",
        "UUCESWI": "Title block should reflect actual work included",
        "BestPractice": "Include notes 'Scope includes/excludes' or detail list in title block",
        "diagnostic": {
            "likely_cause": "Drawing title reused or generic, not updated for this revision",
            "risk": "Site team may assume incorrect scope and perform extra or missing work",
            "fix": [
                "Update drawing title and scope notes to match actual design",
                "Add a scope summary box or general notes entry"
            ]
        }
    },
    "construction_methodology": {
        "description": "Drawing coordinated with construction methodology and RAMS",
        "category": "General",
        "CESWI": "Clause 130.3.1",
        "UUCESWI": "Critical works should align with the method statement",
        "BestPractice": "Add construction staging notes or references to RAMS documents",
        "diagnostic": {
            "likely_cause": "Designer worked without method statement guidance",
            "risk": "Design may conflict with safe or staged construction sequence",
            "fix": [
                "Include notes on installation order (e.g., 'Install A before B')",
                "Reference RAMS document numbers or section in notes"
            ]
        }
    },
    "services_buildable": {
        "description": "All services, structures, and components are shown logically and are buildable",
        "category": "Combined",
        "CESWI": "Clause 130.5.1",
        "UUCESWI": "Designs must be constructable in a logical sequence",
        "BestPractice": "Review overall layout for clashes and sequence feasibility with site team",
        "diagnostic": {
            "likely_cause": "Layout was not reviewed for constructability",
            "risk": "Unbuildable details or unsafe installation sequences go unnoticed",
            "fix": [
                "Walk through the build sequence with a modeller or foreman",
                "Simplify overly complex intersections or details"
            ]
        }
    },
    "omissions_ambiguities": {
        "description": "Check for any missing details, ambiguities, or risks on the drawing",
        "category": "General",
        "CESWI": "Clause 130.7.1",
        "UUCESWI": "Designs must be complete and unambiguous",
        "BestPractice": "Peer-review drawings or use checklist to catch omissions before IFC",
        "diagnostic": {
            "likely_cause": "Drawing issued without full coordination or review",
            "risk": "Site delays or unsafe improvisation due to missing info",
            "fix": [
                "Review drawing in detail for missing dimensions or notes",
                "Add any missing callouts, dimensions, or clarifying annotations"
            ]
        }
    }
,
"penetration_required": {
    "description": "Wall sleeve required at each wall penetration",
    "category": "Combined",
    "CESWI": "Clause 502.2.4",
    "UUCESWI": "WIMES 3.02 Clause 2.1",
    "BestPractice": "Use sleeve pipe penetration details at all wall entries",
    "diagnostic": {
        "likely_cause": "Pipe or cable entering wall without protection",
        "risk": "Leaks or structural damage from unsealed penetration",
        "fix": [
            "Add penetration detail showing sleeve and sealant",
            "Check for clash with reinforcement or wall rebar zones"
        ]
    }
},
"pipe_clearance_min": {
    "description": "Minimum clearance between pipe/duct and structure maintained",
    "category": "Civils",
    "CESWI": "Table 6.1",
    "UUCESWI": "UUCESWI Issue 7 – 300mm clearance recommended",
    "BestPractice": "Maintain 300mm minimum between pipe and structural wall/slab",
    "diagnostic": {
        "likely_cause": "Pipe route too close to concrete or foundation",
        "risk": "Difficult installation or concrete breakout required",
        "fix": [
            "Shift pipe to maintain clearance zone",
            "Update drawing to show minimum clearance callout"
        ]
    }
}
}
```json

