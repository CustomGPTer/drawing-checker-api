qa_checks = {
    "pipe_layout": {
        "description": "Pipe layout shown clearly using polylines or linear entities",
        "category": "Civils",
        "CESWI": "Clause 505.1.2",
        "UUCESWI": "Clause 505.1.2 – Use LWPOLYLINE for pipe alignment overlays",
        "BestPractice": "Use distinct layers and continuous line types for pipe alignment",
        "diagnostic": {
            "likely_cause": "Pipe layout not created or not exported correctly",
            "risk": "Incorrect pipe routing on site",
            "fix": [
                "Ensure all pipe runs are LWPOLYLINE type",
                "Use a dedicated pipe layout layer"
            ]
        }
    },
    "invert_levels": {
        "description": "Invert and cover levels shown at every MH or pipe run",
        "category": "Civils",
        "CESWI": "Clause 505.3.1",
        "UUCESWI": "Clause 505.3.1 – All MHs must show cover + invert levels",
        "BestPractice": "Show both IL and CL on plan and long section",
        "diagnostic": {
            "likely_cause": "Omitted from drawing or incorrect layer naming",
            "risk": "Incorrect excavation depth or backfall",
            "fix": [
                "Label IL and CL at every chamber and pipe end",
                "Ensure layer name includes 'INV'"
            ]
        }
    },
    "drawing_status": {
        "description": "Drawing is marked as 'For Construction', 'For Info', etc.",
        "category": "General",
        "CESWI": "Clause 130.1",
        "UUCESWI": "Clause 130.1 – Construction drawings must be clearly marked",
        "BestPractice": "Title block should always show revision and status",
        "diagnostic": {
            "likely_cause": "CAD export from wrong version or missing notes",
            "risk": "Wrong drawing used on site",
            "fix": [
                "Add revision and status to drawing frame",
                "Ensure ‘FOR CONSTRUCTION’ is clearly marked"
            ]
        }
    },
    "pipe_bedding": {
        "description": "Correct pipe bedding type specified and shown",
        "category": "Civils",
        "CESWI": "Clause 505.3.1",
        "UUCESWI": "Addendum A – Type B bedding required under roads",
        "BestPractice": "Reference UU STD Detail 6101 or CIRIA C689",
        "diagnostic": {
            "likely_cause": "Bedding note or section omitted",
            "risk": "Incorrect bedding leads to pipe deformation",
            "fix": [
                "Include general note: 'Pipe bedding per CESWI Type B'",
                "Add typical bedding detail cross-section"
            ]
        }
    },
    "flow_direction": {
        "description": "Flow direction clearly indicated along all pipe runs",
        "category": "Civils",
        "CESWI": "Clause 502.1.2",
        "UUCESWI": "Noted in section 5 of UUCESWI",
        "BestPractice": "Arrows every 10–15m on plan view",
        "diagnostic": {
            "likely_cause": "Flow arrows not inserted or layer turned off",
            "risk": "Incorrect pipe fall direction during install",
            "fix": [
                "Add flow arrows on plan and section views",
                "Use a dedicated layer for flow direction"
            ]
        }
    },
    "chamber_refs": {
        "description": "Chamber references match layout and MH schedule",
        "category": "Civils",
        "CESWI": "Clause 505.4.1",
        "UUCESWI": "Match manhole numbering to schedule",
        "BestPractice": "Use unique MH IDs on plan and long section",
        "diagnostic": {
            "likely_cause": "Mismatch between layout and schedule",
            "risk": "Wrong chamber constructed in wrong location",
            "fix": [
                "Check chamber IDs align with MH schedule",
                "Review layout against MH numbering system"
            ]
        }
    },
    "reinforcement": {
        "description": "Reinforcement details shown for slabs, walls, or pads",
        "category": "Civils",
        "CESWI": "Clause 502.3.2",
        "UUCESWI": "Refer to RC detailing notes in civils package",
        "BestPractice": "Use B-series rebar callouts and show bar schedules",
        "diagnostic": {
            "likely_cause": "Missing bar markups or RC overlay",
            "risk": "Incorrect steelwork during pour",
            "fix": [
                "Add rebar layout with bar marks",
                "Reference to bar schedule and spacing"
            ]
        }
    },
    "pipe_material": {
        "description": "Pipe material and jointing clearly labelled",
        "category": "Civils",
        "CESWI": "Clause 505.2.1",
        "UUCESWI": "Use UU-approved materials (e.g. DI, uPVC)",
        "BestPractice": "Add material callout with pipe size and class",
        "diagnostic": {
            "likely_cause": "Generic line used with no annotation",
            "risk": "Wrong pipe type or incorrect pressure class",
            "fix": [
                "Add callouts like '100mm DI PN16 with flange joint'",
                "Match symbols to material legend"
            ]
        }
    },
    "access_ladders": {
        "description": "Access ladders/platforms provided for deep chambers",
        "category": "Access",
        "CESWI": "Clause 509.4.3",
        "UUCESWI": "Comply with working at height procedures",
        "BestPractice": "Show permanent or temporary ladders for access >1.5m",
        "diagnostic": {
            "likely_cause": "Access omitted from structural layout",
            "risk": "Unsafe entry into chamber or void",
            "fix": [
                "Add fixed ladder to sections deeper than 1.2m",
                "Include detail for platform or handhold"
            ]
        }
    },
    "penetrations": {
        "description": "All M&E penetrations shown and coordinated",
        "category": "Coordination",
        "CESWI": "Clause 502.2.4",
        "UUCESWI": "All penetrations must be sleeved and waterproofed",
        "BestPractice": "Use standard sleeve size 2x pipe OD",
        "diagnostic": {
            "likely_cause": "M&E and civils not coordinated",
            "risk": "Late rework or concrete breakout",
            "fix": [
                "Overlay M&E routes onto civils and add sleeves",
                "Include cast-in penetration detail"
            ]
        }
    },
      "valve_positions": {
        "description": "Valves located logically for isolation and maintenance",
        "category": "Mechanical",
        "CESWI": "Clause 508.2.1",
        "UUCESWI": "Isolate all major branches and equipment",
        "BestPractice": "Install valves both upstream/downstream of key assets",
        "diagnostic": {
            "likely_cause": "Valve symbols omitted or generalised",
            "risk": "System can't be isolated safely for repairs",
            "fix": [
                "Add valves at pipe junctions and near plant interfaces",
                "Ensure handle access is shown in plan"
            ]
        }
    },
    "cable_trays": {
        "description": "Cable tray routing shown, free of clashes",
        "category": "Electrical",
        "CESWI": "Clause 512.1.1",
        "UUCESWI": "Cable trays must not obstruct access or vents",
        "BestPractice": "Use 90° bends, max 3% incline, labelled in section",
        "diagnostic": {
            "likely_cause": "Tray layout deferred to contractor",
            "risk": "Unbuildable layout or overhead clashes",
            "fix": [
                "Add plan for main tray routes",
                "Ensure clearance under structures"
            ]
        }
    },
    "duct_spacing": {
        "description": "Cable duct spacing and layout shown correctly",
        "category": "Electrical",
        "CESWI": "Clause 512.1.2",
        "UUCESWI": "Ducts to be spaced min 100mm apart",
        "BestPractice": "Show on plan and typical trench detail",
        "diagnostic": {
            "likely_cause": "Single duct shown, spacing unclear",
            "risk": "Crowded ducts lead to future access issues",
            "fix": [
                "Add duct bank layout and trench section",
                "Specify spacing for HV/LV/comm"
            ]
        }
    },
    "sensor_positions": {
        "description": "Sensors/instruments shown in accurate locations",
        "category": "Instrumentation",
        "CESWI": "Clause 513.2.1",
        "UUCESWI": "Match sensor types to P&ID and field layout",
        "BestPractice": "Include probe depths, mounting brackets",
        "diagnostic": {
            "likely_cause": "Sensor types not known at drawing time",
            "risk": "Wrong sensor positions or installation delay",
            "fix": [
                "Mark probes, flowmeters, temp and pH sensors",
                "Confirm heights and install methods"
            ]
        }
    },
    "flange_orientation": {
        "description": "Flange bolt holes oriented correctly (12 o'clock)",
        "category": "Mechanical",
        "CESWI": "Clause 508.1.5",
        "UUCESWI": "Flanges to align vertically where visible",
        "BestPractice": "Add note: ‘Orient flange bolt holes to vertical’",
        "diagnostic": {
            "likely_cause": "Standard flange symbol used without orientation",
            "risk": "Misaligned flanges cause site fit issues",
            "fix": [
                "Add flange orientation arrows or notes",
                "Use UU STD flange detail"
            ]
        }
    },
    "fall_direction": {
        "description": "Pipe gradients and fall direction shown and buildable",
        "category": "Civils",
        "CESWI": "Clause 505.3.2",
        "UUCESWI": "Minimum falls per pipe size must be respected",
        "BestPractice": "Show % fall on long section or next to pipe",
        "diagnostic": {
            "likely_cause": "Fall left implicit or forgotten",
            "risk": "Backfalls or poor flow performance",
            "fix": [
                "Add pipe gradient next to size (e.g., 150mm @ 1.65%)",
                "Confirm fall exceeds minimum"
            ]
        }
    },
    "access_for_maintenance": {
        "description": "All equipment accessible for future maintenance",
        "category": "Access",
        "CESWI": "Clause 509.3.1",
        "UUCESWI": "1m clearance minimum around maintainable equipment",
        "BestPractice": "Mark hatch or shaded areas showing access zones",
        "diagnostic": {
            "likely_cause": "Maintenance access not considered in layout",
            "risk": "Difficult or unsafe plant access",
            "fix": [
                "Draw 1m clearance around blowers, MCCs, valves",
                "Add note: ‘Maintain access zone for operatives’"
            ]
        }
    },
    "control_panels": {
        "description": "Control panels located with clear cable paths",
        "category": "Electrical",
        "CESWI": "Clause 512.3.1",
        "UUCESWI": "No panel to obstruct routes or overlap safety zones",
        "BestPractice": "Show cable entry from floor/wall",
        "diagnostic": {
            "likely_cause": "Panel blocks or access areas not drawn",
            "risk": "Delayed install or re-routing cables",
            "fix": [
                "Add panel outline to walls with door swing",
                "Check space for maintenance and terminations"
            ]
        }
    },
    "bonding": {
        "description": "Earthing, bonding, and lightning protection shown",
        "category": "Electrical",
        "CESWI": "Clause 512.5.1",
        "UUCESWI": "See WIMES 1.02 for bonding requirement",
        "BestPractice": "Bond all metallic pipe, tank, tray, support steel",
        "diagnostic": {
            "likely_cause": "Earthing system designed separately",
            "risk": "Electrical non-compliance or unsafe discharge",
            "fix": [
                "Add earthing/bonding symbol to all applicable assets",
                "Include schematic of bonding system"
            ]
        }
    },
    "vent_routes": {
        "description": "Vent and overflow pipes routed logically",
        "category": "Mechanical",
        "CESWI": "Clause 508.4.1",
        "UUCESWI": "Overflows must not discharge to surface water",
        "BestPractice": "Mark pipe ends with vent/overflow label",
        "diagnostic": {
            "likely_cause": "Overflow/vent routes not coordinated",
            "risk": "Discharge to wrong system or clash risk",
            "fix": [
                "Ensure overflow connects to storm or return system",
                "Add air valve and vent point details"
            ]
        }
    },
    "buildability": {
        "description": "Overall buildability of the drawing",
        "category": "General",
        "CESWI": "Clause 130.5.1",
        "UUCESWI": "Designs must be constructable in logical sequence",
        "BestPractice": "Pre-check constructability with site team",
        "diagnostic": {
            "likely_cause": "Designer unfamiliar with field build",
            "risk": "Unbuildable or unsafe sequences",
            "fix": [
                "Add build stages or install order if complex",
                "Review with construction team before IFC"
            ]
        }
    },
    "scope_defined": {
        "description": "Scope of drawing clearly defined in title and notes",
        "category": "General",
        "CESWI": "Clause 130.2.2",
        "UUCESWI": "Title block to reflect actual scope",
        "BestPractice": "Notes should define what is and isn’t included",
        "diagnostic": {
            "likely_cause": "Drawing title reused from prior version",
            "risk": "Wrong assumptions by site team",
            "fix": [
                "Update drawing title to match actual work shown",
                "Use 'scope includes/excludes' note block"
            ]
        }
    },
    "methodology_link": {
        "description": "Drawing coordinated with RAMS or method sequence",
        "category": "General",
        "CESWI": "Clause 130.3.1",
        "UUCESWI": "All critical works must align with method statement",
        "BestPractice": "Add construction note if method matters",
        "diagnostic": {
            "likely_cause": "Drawing prepared in isolation from RAMS",
            "risk": "Design contradicts safe or staged install",
            "fix": [
                "Add build order or ‘Install A before B’ note",
                "Reference RAMS ID or sheet"
            ]
        }
    },
    "temporary_works": {
        "description": "Notes on temporary works, if required",
        "category": "General",
        "CESWI": "Clause 130.4.1",
        "UUCESWI": "TW required for any excavation >1.2m or backpropping",
        "BestPractice": "Note TW by others, or add TW design reference",
        "diagnostic": {
            "likely_cause": "TW assumed outside design scope",
            "risk": "Unsafe dig or unsupported structure",
            "fix": [
                "Note: ‘TW design by contractor’ or add detail",
                "Add typical shoring if standard"
            ]
        }
    },
    "lifting_zones": {
        "description": "Lifting access and exclusion zones identified",
        "category": "Access",
        "CESWI": "Clause 509.5.2",
        "UUCESWI": "Exclusion zones required for overhead lifting",
        "BestPractice": "Mark swing area and crane pads",
        "diagnostic": {
            "likely_cause": "Lifting route not planned in drawing stage",
            "risk": "Unsafe lift or delayed method",
            "fix": [
                "Add note: 'Lifting zone to be cleared'",
                "Use dashed line to mark lifting envelope"
            ]
        }
    },
    "fall_protection": {
        "description": "Fall protection shown for open edges and platforms",
        "category": "Access",
        "CESWI": "Clause 509.1.4",
        "UUCESWI": "Guardrails required for platforms above 600mm",
        "BestPractice": "Show handrail, kickboard in side view",
        "diagnostic": {
            "likely_cause": "Platform design finalised separately",
            "risk": "Open edge left unprotected on site",
            "fix": [
                "Add handrail symbol and height note",
                "Confirm platform compliant to BS EN 13374"
            ]
        }
    },
      "referenced_drawings": {
        "description": "Referenced drawings are listed and up to date",
        "category": "General",
        "CESWI": "Clause 130.6.1",
        "UUCESWI": "All drawings must show up-to-date references",
        "BestPractice": "Reference all supporting drawings in a notes block",
        "diagnostic": {
            "likely_cause": "Drawing index not maintained during revision",
            "risk": "Construction based on outdated or conflicting drawings",
            "fix": [
                "Add drawing reference list to title block or general notes",
                "Cross-check with latest document issue register"
            ]
        }
    },
    "standard_detail_refs": {
        "description": "UU standard detail references correctly applied",
        "category": "Compliance",
        "CESWI": "Clause 505.1.1",
        "UUCESWI": "All construction details must match UU STD references",
        "BestPractice": "Use STD codes like 'STD 6101' in callouts or notes",
        "diagnostic": {
            "likely_cause": "Generic or legacy detail callouts used",
            "risk": "Non-compliant construction or rejected inspections",
            "fix": [
                "Update all detail references to current UU STD numbers",
                "Include callout like 'See STD 6202 for thrust blocks'"
            ]
        }
    },
    "omissions_or_ambiguities": {
        "description": "Check for missing details or unclear instructions",
        "category": "General",
        "CESWI": "Clause 130.7.1",
        "UUCESWI": "Designs must be unambiguous and complete",
        "BestPractice": "Peer review all drawings before IFC",
        "diagnostic": {
            "likely_cause": "Drawing issued before full coordination",
            "risk": "Site delays or unsafe improvisation",
            "fix": [
                "Review drawing as if building from it with no assumptions",
                "Add missing dimensions, notes, or views"
            ]
        }
    },
    "is_current_revision": {
        "description": "Drawing is the current construction issue revision",
        "category": "General",
        "CESWI": "Clause 130.1.4",
        "UUCESWI": "Only Rev ‘C’ or 'P## FOR CONSTRUCTION' may be used",
        "BestPractice": "Show Rev and Issue Date on all pages",
        "diagnostic": {
            "likely_cause": "Rev not updated in title block or overwritten PDF",
            "risk": "Outdated design issued to site",
            "fix": [
                "Confirm with document control which rev is latest",
                "Add note: 'Do not use for construction unless status is current'"
            ]
        }
    }
}




