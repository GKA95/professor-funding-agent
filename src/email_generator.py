def generate_email(professor, profile):
    # Safe starter template. Later this function can be connected to an AI
    # provider to personalize the research paragraph.
    subject = f"Prospective Graduate Student – {professor.research_area or 'Energy Systems'}"

    body = f"""Dear Professor {professor.name.split()[-1] if professor.name else ''},

I am Gideon Kwesi Ansah, an Electrical Engineering graduate with research and project experience in energy systems, renewable energy, machine learning, and energy forecasting.

I came across your work at {professor.university}, particularly your research in {professor.research_area or 'energy systems'}, and I am very interested in the possibility of pursuing graduate research under your supervision.

My background includes work on solar PV and battery systems, energy forecasting using machine learning, and power/energy-related engineering projects. I am currently seeking a fully funded graduate research opportunity.

Could you please let me know whether you expect to have funded Master's or PhD research opportunities for prospective students?

I would be grateful for the opportunity to share my CV and discuss whether my background could fit your research group.

Kind regards,
Gideon Kwesi Ansah
"""
    return subject, body
