from app.models.kpm_transport import KPMEmployee, KPMTruck
from app.models.mr_transport import MREmployee, MRTruck

customer_models = {
    "kpm_transport": {
        "truck": KPMTruck,
        "employee": KPMEmployee,
    },
    "mr_transport": {
        "truck": MRTruck,
        "employee": MREmployee,
    }
}
