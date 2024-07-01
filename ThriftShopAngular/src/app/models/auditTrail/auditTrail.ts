export class BaseAuditTrailObject {
    createdDate: Date;
    createdByID: number;
    createdByName: string | null;
    modifiedDate : Date;
    modifiedByID: number;
    modifiedByName: string | null;
}